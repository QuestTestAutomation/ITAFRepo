from git import Repo
import git
import os
import time
from git import *

LocalRepositoryName = "Local"
LocalDirectoryPath = 'C:\\Devworkspace\\GitWorkspace\\RepOne\\Rep13'
LocalGITRepo = 'C:\\Users\\SANUMOLU'
giturl =  'https://github.com/seshikanth/RepoOne.git'
sourcepath = 'C:\\Devworkspace\\GitWorkspace\\files\\'


repo = git.Repo(giturl) #create repo object of the other repository
repo.git.checkout('remote_to_push/master') #checkout to a branch linked to the other repo
files = os.listdir(LocalDirectoryPath)

print(files)

for file in files:
    print(file)
    repo.git.add(file)
#file = 'path/to/file' #path to file to push
#repo.git.add(file) # same as git add file
repo.git.commit(m = "commit message") # same as git commit -m "commit message"
repo.git.push('remote_to_push', 'HEAD:master') # git push remote_to_push HEAD:master