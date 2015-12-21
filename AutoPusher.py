__author__ = 'saipc'

import os
import subprocess

def checkFilesForPush(dirName, fileNamePattern):
    os.chdir(dirName)
    folderList=os.listdir(r"./")
    count = 0
    reposCount = 0
    reposToPush = []

    # iterate thru each folder and check for the repos that we need to push
    for folderName in folderList:
        # cycle through the project folders
        if os.path.isdir(folderName) and folderName.endswith(fileNamePattern):
            print folderName
            os.chdir(folderName)
            # cycle through and find the repos to be pushed
            repos = os.listdir(r".")
            for repo in repos:
                if os.path.isdir(repo) and not repo.startswith('.'):
                    os.chdir(repo)
                    status = subprocess.call('git s | clear', shell=True)
                    # print status
                    print repo
                    # git repo
                    if status != 128:
                        # need to check for add/track/push
                        print "Git repo"
                        pushStatus = subprocess.call('git s | egrep --color=auto \'(Changes to be committed)|(untrack)|(use "git push" to publish your local commits)\'', shell=True)
                        print pushStatus
                        if pushStatus == 0:
                            print "Found Repo to add/track/push"
                            reposToPush.append(repo)
                            reposCount += 1
                    else:
                        # not a git repo
                        print "Not a Git repo"
                    # go back to parent and continue
                    os.chdir(r"../")
                    count += 1
            # go back to parent and continue
            os.chdir(r"../")
    print count, "folders checked"
    print reposCount, "repos found"
    print reposToPush
    #
    #     # theoretically this should work, it worked for the file i compiled myself to a.out
    #     # now if we can have all the .out files in the directories, we can simply check for all mem leaks :D
    #     filePath = os.path.join(dirName, folderName, "a.out")
    #     fullFilePathCommand= r"/Users/schandramouli/PycharmProjects/Python_AutomatedCorrectors/script.sh " + filePath
    #     retVal = subprocess.call('bash ' + fullFilePathCommand, shell=True)
    #     print retVal



checkFilesForPush(r"../", "RubymineProjects")
