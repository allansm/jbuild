import dependency

from argsHandle import *
from fileHandle import *
from os import system,chdir

args = getArgs(["file","?runnable","?r"])

jar = "jar cvf"

if(args.runnable or args.r):
    jar+="e"

remove("build")
mkdir("build")

jar+=" ../build/"

name = getFileName(args.file).split(".")[0].lower()+".jar"

jar+=name

if(args.runnable or args.r):
    jar+=" "+args.file.replace("/",".").replace("\\",".").replace(".class","")
jar+=" "+args.file
print(jar)
chdir("bin")
system(jar)
