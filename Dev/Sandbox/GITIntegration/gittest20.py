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
DirectoryName = "Hello999991"
destinationpath = LocalDirectoryPath + '\\' +  DirectoryName
RepositoryName = "RepOne"

gitlib = GITLibrary.gitlibrary()
r = Repo.clone_from(giturl, LocalRepoPath)

#os.chdir(destinationpath)

#InitializeRepository(LocalGITRepo, LocalDirectoryPath)
time.sleep(2)
gitlib.adddirectorytorepository(gitlib,LocalGITRepo, LocalDirectoryPath, DirectoryName)
gitlib.copy_files(gitlib,sourcepath, destinationpath)
os.chdir(destinationpath)
time.sleep(2)
gitlib.addallfilestorepository(gitlib,LocalGITRepo, LocalDirectoryPath,destinationpath)
#addfilestorepository(LocalGITRepo, LocalDirectoryPath)
# remoterepo = git.Repo(LocalDirectoryPath)
# remoterepo.git.push(refspec='master:master')
# remoterepo.remotes
# remoterepo.origin.push(refspec='master:master')


r.remotes.origin.push()
#cleanupdirectory(LocalDirectoryPath)
#gitlib.deletefolders(LocalDirectoryPath)

