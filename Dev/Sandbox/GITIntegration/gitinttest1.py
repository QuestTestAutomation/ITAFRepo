"""



import git
repo = git.Repo( '/home/questtesting/Rep1' )
print(repo.git.status())
"""
"""
from git import Repo
import od

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
#repo = Repo(self.rorepo.working_tree_dir)
#assert not repo.bare

bare_repo = Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
assert bare_repo.bare
"""

from git import Repo
import os
print("***" + os.getcwd())
r = Repo("https://github.com/questtesting/Rep1.git")
repo_heads = r.heads # or it's alias: r.branches