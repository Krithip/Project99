import os
import shutil
#for removing files
import time
def main():
    deletedFolderCount = 0
    deletedFilesCount = 0
    path = "/PATH_TO_DELETE"
    days = 1
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount += 1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds>= get_file_or_folder_age(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount += 1
                for file in files:
                    filePath = ospath.join(rootFolder, file)
                    if seconds>= get_file_or_folder_age(filePath):
                        removeFile(filePath)
                        deletedFilesCount += 1
        else:
            if seconds>= get_file_or_folder_age(path):
                removeFile(path)
                deletedFilesCount += 1
    else:
        print("Path not found")
        deletedFilesCount += 1
    print(deletedFolderCount)
    print(deletedFilesCount)
def removeFolder():
    if not shutil.rmtree(path):
        print("Folder removed successfully")
    else:
        print("Unable to remove folder")
def removeFile():
    if not os.remove(path):
        print("FIle deleted successfully")
    else:
        print("Unable to remove file")
def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime
if __name__=="__main__":
    main()