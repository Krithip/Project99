import os
import shutil
source = input("Which folder would you like to organize?")
listofFiles = os.listdir(source)
for file in listofFiles:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(source+'/'+ext):
        shutil.move(source+'/'+file,source+'/'+ext+'/'+file)
    else:
        os.makedirs(source+'/'+ext)
        shutil.move(source+'/'+file, source+'/'+ext+'/'+file)