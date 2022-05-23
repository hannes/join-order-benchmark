import pyodbc
import glob
queries = 'explicit'
files = glob.glob(f"{queries}/[0-9]*.sql")
files.sort()

server = 'tcp:localhost'
username = 'sa'
password = 'fD7zF3pM4xB9xD7c'
# obvsl needs updating
driver = '/export/scratch2/home/hannes/join-order-benchmark/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';UID='+username+';PWD='+ password)
con = cnxn.cursor()

def op_inspect(res):
  cost = 0
  for row in res:
    op = row[7]
    n = row[0]
    if op != 'Inner Join':
      continue
    cost += n
  return cost

for f in files:
  with open(f, 'r') as file:
    query_string = file.read()
    try:
      con.execute("SET STATISTICS PROFILE ON; %s" % query_string)
      con.nextset()
      explain = con.fetchall()

      print("sqlserver\t%s\t%d" % (f.replace('.sql', '').replace(f'{queries}/',''), op_inspect(explain)))
    except:
      print("sqlserver\t%s\t" % (f.replace('.sql', '').replace(f'{queries}/','')))