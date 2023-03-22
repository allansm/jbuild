def main():
    from allansm.jbuild import writeFile, readFile, ls, getLines, getAllFiles, isWindows, mkdir, remove, classpath, exists, dirname
    from os import system, chdir
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("package")
    parser.add_argument("--runnable", action="store_true", dest="runnable")
    parser.add_argument("--r", action="store_true", dest="r")
    parser.add_argument("--all", action="store_true", dest="all")
    parser.add_argument("--build", action="store_true", dest="build")

    args = parser.parse_args()

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
        try:
            remove("MANIFEST.MF")
        except:
            e=0

        writeFile("MANIFEST.MF",manifest)

        print(readFile("MANIFEST.MF"))

    system(jar)

    remove("MANIFEST.MF")
