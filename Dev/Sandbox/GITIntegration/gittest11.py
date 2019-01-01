import git
import os
import time
from git import *

LocalRepositoryName = "Local"
LocalDirectoryPath = 'C:\\Devworkspace\\GitWorkspace\\RepOne\\Rep13'
LocalGITRepo = 'C:\\Users\\SANUMOLU'
giturl =  'https://github.com/seshikanth/RepoOne.git'

repo = git.Repo(LocalGITRepo)
origin = repo.remotes.origin

assert origin == repo.remotes.origin
origin.fetch()                  # assure we actually have data. fetch() returns useful information
print(origin.fetch())
origin.push()