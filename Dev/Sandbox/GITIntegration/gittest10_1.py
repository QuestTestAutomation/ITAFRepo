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
DirectoryName = "Hello99;/"
destinationpath = LocalDirectoryPath + '\\' +  DirectoryName
RepositoryName = RepOne


def copy_files(sourcepath, destinationpath):
    files = os.listdir(sourcepath)
    print(files)

    for f in files:
        shutil.copy(sourcepath + f, destinationpath)


def InitializeRepository(LocalGITRepo, Localdirectorypath):
    repo = git.Repo(LocalGITRepo)
    repo.init(LocalDirectoryPath, mkdir=True)


def addfilestorepository(LocalGITRepo, LocalDirectoryPath):
    repo = Repo(LocalDirectoryPath)
    files = os.listdir(LocalDirectoryPath)

    print(files)

    for file in files:
        repo.git.add(LocalDirectoryPath + '\\' + DirectoryName + '\\' + file)
    repo.index.commit("First Commit files")

def addallfilestorepository(LocalGITRepo, LocalDirectoryPath,destinationpath):
    os.chdir(destinationpath)
    repo = Repo(LocalDirectoryPath)
    repo.git.add("-A")

    repo.index.commit("First Commit files")


def adddirectorytorepository(LocalGITRepo, LocalDirectoryPath, DirectoryName):
    if os.path.isdir(LocalDirectoryPath):
        print("directory exists")
    else:
        os.mkdir(LocalDirectoryPath + '\\' + DirectoryName)

    repo = Repo(LocalDirectoryPath)
    repo.git.add(LocalDirectoryPath + '\\' + DirectoryName)
    repo.index.commit("Folder added")

def cleanupdirectoryfile(LocalDirectoryFilePath):
    if os.path.isfile(LocalDirectoryFilePath):
        os.remove(LocalDirectoryFilePath)
    else:  ## Show an error ##
        print("Error: %s file not found" % LocalDirectoryFilePath)

def cleanupdirectory(LocalDirectoryPath):
    if os.path.isdir(LocalDirectoryPath):
        print("Directory Exists")
        os.remove(LocalDirectoryPath)

def deletefolders(LocalDirectoryPath):
    os.chdir('C:\\Devworkspace\\GitWorkspace')
    folder_path = LocalDirectoryPath
    for file_object in os.listdir(folder_path):
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)
        else:
            shutil.rmtree(file_object_path)


def CloneRepository():
    repo = Repo.clone_from(cloneUrl, localRepopath)
    remote = repo.create_remote(remote_name, url=another_url)
    remote.push(refspec='{}:{}'.format(local_branch, remote_branch))
#deletefolders(LocalDirectoryPath)
#cleanupdirectory(LocalDirectoryPath)
r = Repo.clone_from(giturl, LocalRepoPath)

#os.chdir(destinationpath)

#InitializeRepository(LocalGITRepo, LocalDirectoryPath)
time.sleep(2)
adddirectorytorepository(LocalGITRepo, LocalDirectoryPath, DirectoryName)
copy_files(sourcepath, destinationpath)
os.chdir(destinationpath)
time.sleep(2)
addallfilestorepository(LocalGITRepo, LocalDirectoryPath,destinationpath)
#addfilestorepository(LocalGITRepo, LocalDirectoryPath)
# remoterepo = git.Repo(LocalDirectoryPath)
# remoterepo.git.push(refspec='master:master')
# remoterepo.remotes
# remoterepo.origin.push(refspec='master:master')


r.remotes.origin.push()
#cleanupdirectory(LocalDirectoryPath)
deletefolders(LocalDirectoryPath)


# repo = Repo(LocalDirectoryPath)
# repo.index.commit("First Commit")

"""   

#if not os.path.exists(LocalDirectoryPath):
#    os.makedirs(LocalDirectoryPath)

#repo = git.Repo('C:\\Users\\SANUMOLU')
#repo.init(LocalDirectoryPath,mkdir=True)
repo = Repo(LocalDirectoryPath)
files = os.listdir(LocalDirectoryPath)

print(files)


for f in files:
        repo.git.add(LocalDirectoryPath + '\\' + f)

#repo.commit()
repo.git.commit('-m', 'test commit')
"""

"""
#time.sleep(10)
files = os.listdir(LocalDirectoryPath)

print(files)

for f in files:
        repo.git.add(LocalDirectoryPath + '\\' + f)

"""

"""
#repo = git.repo(giturl)

#origin = repo.create_remote('origin', 'https://github.com/seshikanth/RepoOne.git')
#repo.init(LocalDirectoryPath,mkdir='True')
repo.add
repo.add(LocalDirectoryPath)
#repo.commit(rev=None)
repo.git.commit('-m', 'test commit')

#repo.git.commit('-m', 'test commit', author='sunilt@xxx.com')

#repo.git.push("origin", "HEAD:refs/for/master")
"""