import jbuild

import os
from subprocess import call
from jcore import *

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--args", required=False)
parser.add_argument("--index", required=False)

args = parser.parse_args()

suffix=":"
if(isWindows()):
    suffix=";"

bin = getAllFiles("bin")

i = 0

package = []

for b in bin:
    p = b.split(".")[0]
    p2 = p.split("/")
    tmp = "."
    tmp = tmp.join(p2)
    package.append(tmp.replace("bin.",""))
    print(str(i)+" : "+package[i])
    i = i + 1

index = args.index

if(index == None):
    if(len(package) == 1):
        index = 0
    else:
        index = int(input("index:"))
else:
    index = int(index)

cn = package[index].split(".")[-1]

remove("bat/"+cn+".bat")
remove("bash/"+cn)

mkdir("bat")
mkdir("bash")

cp = "\"src"+suffix+"bin"
cplib = ""

if(exists("lib")):
    cp+=suffix+"lib"
    lib = getAllFiles("lib")
    for f in lib:
        cplib+=suffix+f

if(exists(".lib")):
    for x in getLines(".lib"):
        cplib+=suffix+x
        
cp+=cplib

cp+="\""

call("echo @echo off > bat/"+cn+".bat",shell=True)
call("echo cd .. >> bat/"+cn+".bat",shell=True)
call("echo java -classpath "+cp+" "+package[index]+" >> bat/"+cn+".bat",shell=True)

call("echo #!/bin/bash > bash/"+cn ,shell=True)
call("echo cd .. >> bash/"+cn, shell=True)
call("echo java -classpath "+cp+" "+package[index]+" >> bash/"+cn, shell=True)


print("running...\n")

if(args.args != None):
    call("java -classpath "+cp+" "+package[index]+" "+args.args,shell=True)
else:
    call("java -classpath "+cp+" "+package[index],shell=True)

