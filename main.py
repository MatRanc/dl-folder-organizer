import os
import shutil
from glob import glob
from pathlib import Path

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)

#make screenshots folder
print("Making screenshots folder")
screenshots_folder = "screenshots/"
os.makedirs("screenshots")
print("Screenshots folder created")

for x in glob("Screen Shot*"):
    source = path+"/"+x
    destination = "screenshots/"

    print(x)
    shutil.move(source, destination)

print("done")