import git
import os

LocalRepositoryName = "Local"
LocalDirectoryPath = 'C:\\Devworkspace\\GitWorkspace\\RepOne\\Rep1000'
LocalGITRepo = 'C:\\Users\\SANUMOLU'
giturl =  'https://github.com/seshikanth/RepoOne.git'

repo = git.Repo('C:\\Users\\SANUMOLU')
#repo = git.repo(giturl)

#origin = repo.create_remote('origin', 'https://github.com/seshikanth/RepoOne.git')
#repo.init(LocalDirectoryPath,mkdir='True')
#repo.git.add(LocalDirectoryPath)
#repo.commit(rev=None)
repo.git.commit('-m', 'test commit')

#repo.git.commit('-m', 'test commit', author='sunilt@xxx.com')

#repo.git.push("origin", "HEAD:refs/for/master")
