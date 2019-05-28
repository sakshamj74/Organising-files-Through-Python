import os,shutil

dest1=r'/home/sak/Documents/Movies'
if not os.path.exists(dest1):
	os.makedirs(dest1)
s='/home/sak/Documents/'
r=s
source=os.listdir(s)
for files in source:
	if files.endswith(".mkv"):	
		shutil.copy(s+str(files), dest1)
		os.chdir(r)
		os.remove(s+str(files))

dest2=r'/home/sak/Documents/Documents'
if not os.path.exists(dest2):
	os.makedirs(dest2)
s='/home/sak/Documents/'
r=s
source=os.listdir(s)
for files in source:
	if files.endswith("pdf") or files.endswith(".docx") or files.endswith(".txt"):	
		shutil.copy(s+str(files), dest2)
		os.chdir(r)
		os.remove(s+str(files))


dest1=r'/home/sak/Documents/songs'
if not os.path.exists(dest1):
	os.makedirs(dest1)
s='/home/sak/Documents/'
r=s
source=os.listdir(s)
for files in source:
	if files.endswith(".mp4"):	
		shutil.copy(s+str(files), dest1)
		os.chdir(r)
		os.remove(s+str(files))

dest1=r'/home/sak/Documents/PY_files'
if not os.path.exists(dest1):
	os.makedirs(dest1)
s='/home/sak/Documents/'
r=s
source=os.listdir(s)
for files in source:
	if files.endswith(".py"):	
		shutil.copy(s+str(files), dest1)
		os.chdir(r)
		os.remove(s+str(files))

dest1=r'/home/sak/Documents/Photos'
if not os.path.exists(dest1):
	os.makedirs(dest1)
s='/home/sak/Documents/'
r=s
source=os.listdir(s)
for files in source:
	if files.endswith(".jpg"):	
		shutil.copy(s+str(files), dest1)
		os.chdir(r)
		os.remove(s+str(files))




		
                	

		

