import glob
files = glob.glob("[0-9]*.sql")
files.sort()

for f in files:
	with open(f, 'r') as file:
   		data = file.read().replace('\n', '\\n').replace('"', '\\"')
   		print('/* '+f+' */ "' + data + '",',)
