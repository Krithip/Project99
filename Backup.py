import os
import shutil
source = input("Enter the folder name")
destination = input("Enter the destination folder name")
source = source + '/'
destination = destination + '/'
listofFiles = os.listdir(source)
for file in listofFiles:
    shutil.copy((source+file), destination)