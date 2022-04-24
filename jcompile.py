import os
from jcore import *
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

for line in javac:
    os.system("javac -d bin "+line)
