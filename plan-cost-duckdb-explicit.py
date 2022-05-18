import duckdb
import json
import glob
import os
files = glob.glob("explicit/[0-9]*.sql")
files.sort()
# FIXME
#files = ['01a.sql']

profile_filename = 'duckdb_profile.json'

con = duckdb.connect("job.duckdb", read_only=True)

#os.remove(profile_filename)
con.execute("SET disabled_optimizers TO 'join_order'")
con.execute('PRAGMA enable_profiling=json')
con.execute("PRAGMA profile_output='%s'" % profile_filename)


def op_inspect(op):
  cost = 0
  if op['name'] == 'HASH_JOIN' and not op['extra_info'].startswith('MARK'):
    cost = op['cardinality']
  if 'children' not in op:
    return cost
  for child_op in op['children']:
    cost += op_inspect(child_op)
  return cost

for f in files:
  with open(f, 'r') as file:
      con.execute(file.read())
      # work around a bug where the profiling file was not there yet, 
      # running another query forces closing the result set
      con.execute("SELECT 42") 

      explain = json.load(open(profile_filename))
      #print(print(json.dumps(explain, indent=4, sort_keys=True)))
      print("duckdb-explicit\t%s\t%d" % (f.replace('.sql', '').replace('explicit/', ''), op_inspect(explain)))
