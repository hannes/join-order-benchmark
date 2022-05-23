import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:localhost'
database = 'Express'
username = 'sa'
password = 'fD7zF3pM4xB9xD7c'
driver = '/export/scratch2/home/hannes/join-order-benchmark/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.7.so.2.1'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

q = '''
SET STATISTICS PROFILE ON;

SELECT  MIN(cast(mc.note as varchar)) AS production_note,
       MIN(cast(t.title as varchar)) AS movie_title,
       MIN(t.production_year) AS movie_year
FROM company_type AS ct,
     info_type AS it,
     movie_companies AS mc,
     movie_info_idx AS mi_idx,
     title AS t
WHERE ct.kind = 'production companies'
  AND it.info = 'top 250 rank'
  AND mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'
  AND (mc.note LIKE '%(co-production)%'
       OR mc.note LIKE '%(presents)%')
  AND ct.id = mc.company_type_id
  AND t.id = mc.movie_id
  AND t.id = mi_idx.movie_id
  AND mc.movie_id = mi_idx.movie_id
  AND it.id = mi_idx.info_type_id;
'''

cursor.execute(q)
# ha
cursor.nextset()

sum = 0
res = cursor.fetchall()
for row in res:
	op = row[7]
	n = row[0]
	if op != 'Inner Join':
		continue

	sum += n

print(sum)