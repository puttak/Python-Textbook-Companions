
import os,sys

rootdir = os.getcwd()


for path,dirname,files  in os.walk(rootdir):
    for file in files: 
        if file.endswith(".ipynb"):
        	filename = file.split('.')
        	version = filename[0].rsplit('_')
        	print version
        	if len(version)>1:
        		try:
        			int(version[-1])
        			file_new = file
        		except ValueError:
        			file_new = file.replace('_'+version[-1],'')
                
                        os.rename(os.path.join(path,file),os.path.join(path,file_new))
