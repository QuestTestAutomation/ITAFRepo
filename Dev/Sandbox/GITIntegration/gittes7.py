


empty_repo = git.Repo.init(osp.join(rw_dir, 'empty'))
origin = empty_repo.create_remote('origin', repo.remotes.origin.url)
assert origin.exists()
assert origin == empty_repo.remotes.origin == empty_repo.remotes['origin']
origin.fetch()                  # assure we actually have data. fetch() returns useful information
# Setup a local tracking branch of a remote branch
empty_repo.create_head('master', origin.refs.master)  # create local branch "master" from remote "master"
empty_repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
empty_repo.heads.master.checkout()  # checkout local "master" to working tree
# Three above commands in one:
empty_repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
# rename remotes
origin.rename('new_origin')
# push and pull behaves similarly to `git push|pull`
origin.pull()
origin.push()