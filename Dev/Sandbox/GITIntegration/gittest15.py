from Sandbox.Libraries.DEV import GITLibrary
import git
import os
import time
from git import *
import shutil


LocalRepositoryName = "Local"
LocalDirectoryPath = 'C:\\Devworkspace\\GitWorkspace\\new\\RepOne'
LocalGITRepo = 'C:\\Users\\SANUMOLU'
giturl = 'https://github.com/seshikanth/RepoOne.git'
sourcepath = 'C:\\Devworkspace\\GitWorkspace\\files\\'
LocalRepoPath = 'C:\\Devworkspace\\GitWorkspace\\new\\RepOne'
DirectoryName = "Hello9920"
destinationpath = LocalDirectoryPath + '\\' +  DirectoryName
RepositoryName = "RepOne"

print("LocalDirectoryPath "  +  str(os.path.isdir(destinationpath)))
print("LocalDirectoryPath1 "  +  str(os.path.exists(destinationpath)))
print("LocalDirectoryPath2 "  +  str(os.path.abspath(destinationpath)))
print("LocalDirectoryPath3 "  +  str(os.path.isdir(os.path.abspath(destinationpath))))
print("LocalDirectoryPath4  "  +  str(os.path.exists(os.path.abspath(destinationpath))))

if os.path.exists(destinationpath):
    print("directory exists")
else:
    os.mkdir(LocalDirectoryPath + '\\' + DirectoryName)