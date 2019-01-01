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