def main():
    from allansm.jbuild import writeFile, readFile, ls, getLines, getAllFiles, isWindows, mkdir, remove, classpath, exists, dirname
    from subprocess import call
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("cp")
    parser.add_argument("package")
    parser.add_argument("--args", required=False)

    args = parser.parse_args()

    args.cp = args.cp.replace("\\","/")

    suffix=":"
    if(isWindows()):
        suffix=";"

    cp = "\""+args.cp+"/bin"+suffix+args.cp+"/lib"

    if(exists("lib")):
        cp+=suffix+"lib"
        lib = getAllFiles("lib")
        for f in lib:
            cplib+=suffix+f

    if(exists(args.cp+"/.lib")):
        for x in getLines(args.cp+"/.lib"):
            cp+=suffix+x
     
    cp+="\""

    if(args.args != None):
        call("java -cp "+cp+" "+args.package+" "+args.args)
    else:
        call("java -cp "+cp+" "+args.package)
