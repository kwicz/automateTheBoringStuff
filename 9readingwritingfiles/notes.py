from pathlib import Path
import os
import shelve


# https://automatetheboringstuff.com/2e/chapter9/

#Get path from home directory
Path.home()

#Make a Directory
Path(r'/Users/katysolovewicz/projects/automatetheboringstuff/readingwritingfiles/newDirectory').mkdir()

#Other way of making a new directory
os.makedirs('/Users/katysolovewicz/projects/automatetheboringstuff/readingwritingfiles/newDirectory')

#Find the current working directory (cwd)
os.getcwd()
#or (better)
Path.cwd()

#Change directory
os.chdir('/Users/katysolovewicz/Projects/AutomateTheBoringStuff')

#Open a file
sonnetFile = open('/Users/katysolovewicz/projects/automatetheboringstuff/readingwritingfiles/sonnet29.txt')

#Read the contents
sonnetContent = sonnetFile.read()
sonnetContents = sonnetFile.readlines()

#Get the file size
sonnetContnet = sonnetFile.getsize()

#Write to the file

#Booleans to check path validitiy
p.exists()
p.is_file()
p.is_dir()

#Open and write write with the shelf module
