import dependency

from argsHandle import *
from fileHandle import *
from os import system,chdir

args = getArgs(["file","?runnable","?r"])

jar = "jar cvf"

if(args.runnable or args.r):
    jar+="m"

jar+=" ../"

name = getFileName(args.file).split(".")[0].lower()+".jar"

jar+=name

manifest = ""
if(args.runnable or args.r):
    mainclass = args.file.replace("/",".").replace("\\",".").replace(".class","")
    jar+=" MANIFEST.MF"

    manifest = "Manifest-Version: 1.0\n"
    manifest+= "Main-Class: "+mainclass+"\n"
    manifest+= "Class-Path:"
    for n in ls("lib"):
        manifest+=" "+n.replace("\\","/")
    manifest+="\n"

jar+=" "+args.file

print(jar)

chdir("bin")

remove("MANIFEST.MF")
writeFile("MANIFEST.MF",manifest)

print(readFile("MANIFEST.MF"))

system(jar)

remove("MANIFEST.MF")
