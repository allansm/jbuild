import jbuild

import os
from subprocess import call
import dependency
from fileHandle import *
from util import *
from argsHandle import *

args = getArgs(["--args","--index"])

bin = getAllFiles("bin")

i = 0

package = []

for b in bin:
    p = b.split(".")[0]
    p2 = p.split("\\")
    tmp = "."
    tmp = tmp.join(p2)
    package.append(tmp.replace("bin.",""))
    print(str(i)+" : "+package[i])
    i = i + 1

index = None
if(args.index == None):
    index = int(input("index:"))
else:
    index = int(args.index)

cn = package[index].split(".")[-1]

try:
    os.mkdir("bat")
except:
    dummy = ""

cp = "\"src;bin"
cplib = ""

if(exists("lib")):
    cp+=";lib"
    lib = getAllFiles("lib")
    for f in lib:
        cplib+=";"+f

if(exists(".lib")):
    for x in getLines(".lib"):
        cplib+=";"+x
        
cp+=cplib

cp+="\""

clear()
call("echo @echo off > bat/"+cn+".bat",shell=True)
call("echo cd .. >> bat/"+cn+".bat",shell=True)
call("echo java -classpath "+cp+" "+package[index]+" >> bat/"+cn+".bat",shell=True)

call("java -classpath "+cp+" "+package[index]+" "+args.args,shell=True)

