from github import Github
import pygit2
username = "questtesting"
password = "Quest@1234"
useremail = "art.cognizant1@gmail.com"
giturl = "https://github.com/questtesting"
readmeText = "Hello Test"
# using username and password establish connection to github
g = Github("Questtesting", "Quest@1234")
org = g.get_organization('questtest')

#create the new repository
repo = org.create_repo("testprotest1", description = "projectDescription" )

#create some new files in the repo
repo.create_file("/README.md", "init commit", readmeText)

#Clone the newly created repo
repoClone = pygit2.clone_repository(repo.git_url, 'C:\Devworkspace\GitWorkspace\GITTEST')

#put the files in the repository here

#Commit it
repoClone.remotes.set_url("origin", repo.clone_url)
index = repoClone.index
index.add_all()
index.write()
author = pygit2.Signature(useremail, useremail)
commiter = pygit2.Signature(useremail, useremail)
tree = index.write_tree()
oid = repoClone.create_commit('refs/heads/master', author, commiter, "init commit",tree,[repoClone.head.get_object().hex])
remote = repoClone.remotes["origin"]
credentials = pygit2.UserPass(userName, password)
remote.credentials = credentials

callbacks=pygit2.RemoteCallbacks(credentials=credentials)

remote.push(['refs/heads/master'],callbacks=callbacks)