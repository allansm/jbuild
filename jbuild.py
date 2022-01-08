import dependency

import os
from fileHandle import *
from shutil import rmtree

src = getAllFiles("src")

try:
    rmtree("bin")
except:
    dummy = ""

os.mkdir("bin")

javac = []

for f in src:
    if ".java" in f:
        javac.append(os.path.dirname(f)+"/"+"*.java")

javac = list(dict.fromkeys(javac))

for line in javac:
    print(line)

cp = "\"src;bin;lib;lib/*"
cplib = ""
'''
if(exists("lib")):
    cp+=";lib"
    lib = getAllFiles("lib")
    for f in lib:
        cplib+=";"+f
'''
if(exists(".lib")):
    for x in getLines(".lib"):
        cplib+=";"+x
 
cp+=cplib

cp+="\""


for line in javac:
    os.system("javac -cp "+cp+" -d bin "+line)
