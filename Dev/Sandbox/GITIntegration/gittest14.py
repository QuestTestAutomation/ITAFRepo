import git
import random
import os

repo_name = 'RepoOne'
branch_name = 'feature4'

remote_repo_addr_git = 'https://github.com/seshikanth/RepoOne.git'
#''git@repo:DevOps/z_sandbox1.git'

no = random.randint(0,1000)
repo = git.Repo.clone_from(remote_repo_addr_git, repo_name)
new_branch = repo.create_head(branch_name)
repo.head.set_reference(new_branch)
os.chdir(repo_name)
open("parasol" + str(no), "w+").write(str(no)) # this is added
print(repo.active_branch)
repo.git.add(A=True)
repo.git.commit(m='okej')
repo.git.push(u='origin feature4')