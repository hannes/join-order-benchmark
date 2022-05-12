import psycopg2
import json
import glob
files = glob.glob("explicit/[0-9]*.sql")
files.sort()
# FIXME
#files = ['01a.sql']

con = psycopg2.connect("dbname=job").cursor()
# disable postgres 'parallel' plans because exchange ops make me sad
con.execute('SET max_parallel_workers_per_gather = 0')
con.execute('SET enable_nestloop to false')
con.execute('SET join_collapse_limit = 1')

def op_inspect(op):
  cost = 0
  if op['Node Type'] == 'Hash Join':
    cost = op['Actual Rows']
  if 'Plans' not in op:
    return cost
  for child_op in op['Plans']:
    cost += op_inspect(child_op)
  return cost

for f in files:
  with open(f, 'r') as file:
      query_string = file.read()
      con.execute("EXPLAIN (FORMAT JSON, ANALYZE TRUE) %s" % query_string)
      explain = con.fetchone()[0][0]
      print("postgres\t%s\t%d" % (f.replace('.sql', '').replace('explicit/',''), op_inspect(explain['Plan'])))
