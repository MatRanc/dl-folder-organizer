import os
import sys
import shutil
from glob import glob
from pathlib import Path

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)

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
    for x in glob("Screen Shot*"):
        source = path+"/"+x
        destination = "screenshots/"

        print("Moving file: "+x)
        shutil.move(source, destination)
        print("Filed moved successfully\n")

confirmation()
folder_creation()
move_files()

#Moved [number of files] in [time]

print("done")