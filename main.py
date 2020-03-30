import os
import shutil

S = str(input(''))

# files = [f for f in os.listdir('.') if os.path.isfile(f)]
# files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
# files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ]
# files = filter(os.path.isfile, os.listdir( os.curdir ))
files = [ f for f in os.listdir(S) if os.path.isfile(os.path.join(S,f)) ]
for f in files:
	temp = f.split(".")
	newPath = S + "/" + temp[-1] + '_files'
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	shutil.move(S+'/'+f, newPath)	