#!/usr/bin/env python
__author__ = 'saipc'

import os
import subprocess
import re

reposToPush = []

def checkFilesForPush(dirName, fileNamePattern):
    count = 0
    print "Searching from ", dirName
    os.chdir(dirName)
    folderList=os.listdir(r"./")
    fileNamePattern = re.compile(fileNamePattern)

    # iterate thru each folder and check for the repos that we need to push
    for folderName in folderList:
        # cycle through the project folders
        if os.path.isdir(folderName) and re.search(fileNamePattern, folderName):
            # print "Searching ", folderName
            os.chdir(folderName)
            # if this itself is a git repo, push
            status = subprocess.call('git s', shell=True)
            if status != 128:
                findPushable(os.path.abspath("."))
                pushReadmeChange()
                count += 1
            # else cycle through and find the repos to be pushed
            repos = os.listdir(r".")
            for repo in repos:
                if os.path.isdir(repo) and not repo.startswith('.'):
                    os.chdir(repo)
                    print repo
                    status = subprocess.call('git s', shell=True)
                    # print status
                    if status != 128:
                        # git repo
                        # need to push
                        findPushable(os.path.abspath("."))
                        # check for readme
                        pushReadmeChange()
                    else:
                        # not a git repo
                        print "Not a Git repo"
                    # go back to parent and continue
                    os.chdir(r"../")
                    count += 1
            # go back to parent and continue
            os.chdir(r"../")
    print count, "folders checked"
    print len(reposToPush), "repos found"
    print reposToPush
    # now push them
    for repo in reposToPush:
        push(repo)

def findPushable(repo):
    print "Git repo"
    pushStatus = subprocess.call('git s | egrep --color=auto \'Your branch is up-to-date\'', shell=True)
    # print pushStatus
    if pushStatus == 1:
        # means not up to date
        print "This repo is not up to date", repo
        reposToPush.append(repo)

def push(repo):
    os.chdir(repo)
    # one final safety net, only push to my repos on github
    isMyRepo = subprocess.call('git remote -v | egrep --color=auto \'(.*)github(.*)TDA\'', shell=True)
    # print isMyRepo
    if isMyRepo == 0:
        pushStatus = subprocess.call('git p', shell=True)
        if pushStatus != 128:
            print pushStatus, repo, "pushed successfully"

def pushReadmeChange():
    # this is to automatically add "README Updated" as a commit message
    pushMessageStatus = subprocess.call('git s | egrep --color=auto \'README\'', shell=True)
    print "This is the readme function", pushMessageStatus
    if pushMessageStatus != 1:
        # means README was changed
        subprocess.call('gg.sh "README Updated" ', shell=True)


checkFilesForPush(os.path.expanduser("~"), r"(Projects)|(Scripts)$")
