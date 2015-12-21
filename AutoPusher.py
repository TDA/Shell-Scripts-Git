__author__ = 'saipc'

import os
import subprocess

def checkFilesForPush(dirName):
    os.chdir(dirName)
    folderList=os.listdir(r"./")

    # iterate thru each folder and check for the repos that we need to push
    for folderName in folderList:
        # cycle through the project folders
        if os.path.isdir(folderName) and folderName.endswith("Projects"):
            print folderName
            os.chdir(folderName)
            # cycle through and find the repos to be pushed
            status = subprocess.call('git s', shell=True)
            print status
            os.chdir(r"../")
    #
    #     # theoretically this should work, it worked for the file i compiled myself to a.out
    #     # now if we can have all the .out files in the directories, we can simply check for all mem leaks :D
    #     filePath = os.path.join(dirName, folderName, "a.out")
    #     fullFilePathCommand= r"/Users/schandramouli/PycharmProjects/Python_AutomatedCorrectors/script.sh " + filePath
    #     retVal = subprocess.call('bash ' + fullFilePathCommand, shell=True)
    #     print retVal



checkFilesForPush(r"../")
