import os
import sys
import shutil
from time import sleep
from glob import glob
from pathlib import Path

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)

files_moved = 0

def confirmation():
    print("Would you like to continue? (y/n)")

    if input() == "y":
        pass
    else:
        sys.exit()

def folder_creation():
    print("Preparing screenshots folder")

    if os.path.isdir("screenshots"):
        print("Folder already exists\n")
    else:
        os.makedirs("screenshots")
        print("Created screenshots folder\n")

def move_files():
    global files_moved

    for x in glob("Screen Shot*"):
        source = path+"/"+x
        destination = "screenshots/"

        print("Moving file: "+x)
        shutil.move(source, destination)
        files_moved +=1 #counts how many files are moved
        print("Filed moved successfully\n")

confirmation()
folder_creation()
sleep(5)
move_files()

#check if file is already there
#Moved [number of files] in [time]
print("done")
print("Moved "+str(files_moved)+" files in "+" seconds")