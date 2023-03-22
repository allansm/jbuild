def main():
    import os
    from allansm.jbuild import writeFile, readFile, ls, getLines, getAllFiles, isWindows, mkdir, remove, classpath, exists, dirname
    from shutil import rmtree

    suffix = ":"

    if(isWindows()):
        suffix=";"

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

    cp = "\"src"+suffix+"bin"+suffix+"lib"+suffix+"lib/*"
    cplib = ""

    if(exists(".lib")):
        for x in getLines(".lib"):
            cplib+=suffix+x
     
    cp+=cplib
    cp+=suffix+classpath()
    cp+="\""

    print("building...")

    for line in javac:
        os.system("javac -cp "+cp+" -d bin "+line)
