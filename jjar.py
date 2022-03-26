from allansm.argsHandle import *
from allansm.fileHandle import *
from os import system,chdir

args = getArgs(["package","?runnable","?r","?all","?build"])

if(args.build):
    import jbuild

jar = "jar cvf"

if(args.runnable or args.r):
    jar+="m"

jar+=" ../"

name = ""
if("." in args.package):
    name = args.package.split(".")[-1].lower()+".jar"
else:
    name = args.package.lower()+".jar"

jar+=name

manifest = ""
if(args.runnable or args.r):
    mainclass = args.package
    jar+=" MANIFEST.MF"

    manifest = "Manifest-Version: 1.0\n"
    manifest+= "Main-Class: "+mainclass+"\n"
    flag = True
    
    for n in ls("lib"):
        if(flag):
            manifest+= "Class-Path:"
            flag = False

        manifest+=" "+n.replace("\\","/")
    
    manifest+="\n"

if(args.all):
    tmp = []
    for n in getAllFiles("bin/"+args.package):
        if(".class" in n):
            tmp.append(dirname(n)+"/*.class")

    tmp = list(dict.fromkeys(tmp))
    for n in tmp:
        jar+=" "+n.replace("bin/","")

else:
    if(exists("bin/"+args.package.replace(".","/")+".class")):
        jar+=" "+args.package.replace(".","/")+".class"
    else:
        jar+=" "+args.package.replace(".","/")+"/*.class"

print(jar)

chdir("bin")

if(args.runnable or args.r):
    remove("MANIFEST.MF")
    writeFile("MANIFEST.MF",manifest)

    print(readFile("MANIFEST.MF"))

system(jar)

remove("MANIFEST.MF")
