__author__ = 'saipc'

import os
import subprocess
import re


reposCount = 0
reposToPush = []
count = 0

def checkFilesForPush(dirName, fileNamePattern):
    print "Searching from ", dirName
    os.chdir(dirName)
    folderList=os.listdir(r"./")
    fileNamePattern = re.compile(fileNamePattern)

    # iterate thru each folder and check for the repos that we need to push
    for folderName in folderList:
        # cycle through the project folders
        if os.path.isdir(folderName) and re.search(fileNamePattern, folderName):
            print "Searching ", folderName
            os.chdir(folderName)
            # if this itself is a git repo, push
            status = subprocess.call('git s', shell=True)
            if status != 128:
                push(folderName)
            # else cycle through and find the repos to be pushed
            repos = os.listdir(r".")
            for repo in repos:
                if os.path.isdir(repo) and not repo.startswith('.'):
                    os.chdir(repo)
                    status = subprocess.call('git s', shell=True)
                    # print status
                    if status != 128:
                        # git repo
                        # need to push
                        push(repo)
                    else:
                        # not a git repo
                        print "Not a Git repo"
                    # go back to parent and continue
                    os.chdir(r"../")
                    # count += 1
            # go back to parent and continue
            os.chdir(r"../")
    print count, "folders checked"
    print reposCount, "repos found"
    print reposToPush
    #

def push(repo):
    print "Git repo"
    pushStatus = subprocess.call('git s | egrep --color=auto \'Your branch is up-to-date\'', shell=True)
    # print pushStatus
    if pushStatus == 1:
        # means not up to date
        print "This repo is not up to date", repo
        reposToPush.append(repo)
        #reposCount += 1

checkFilesForPush(r"../", r"(Projects)|(Scripts)$")
