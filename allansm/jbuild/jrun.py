def main():
    import allansm.jbuild.jbuild as jbuild
    
    jbuild.main()

    import os
    from subprocess import call
    from jcore import writeFile, readFile, ls, getLines, getAllFiles, isWindows, mkdir, remove, classpath, exists, dirname

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
        
        if(not "$" in tmp):
            code = readFile(b.replace("bin", "src").replace("class", "java"))
            flag = False
            for n in code.split("\n"):
                for x in "public static void main".split(" "):
                    if(x in n):
                        flag = True
                    else:
                        flag = False
                        break
                
                if(flag):
                    break
            
            if(flag):
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
    cp+=suffix+classpath()
    cp+="\""

    bat = "@echo off\n"
    bat+= "cd ..\n"
    bat+= "java -classpath "+cp+" "+package[index]

    bash = "#!/bin/bash\n"
    bash+= "cd ..\n"
    bash+= "java -classpath "+cp.replace(";", ":")+" "+package[index]

    writeFile("bat/"+cn+".bat", bat)
    writeFile("bash/"+cn, bash)

    print("running...\n")

    if(args.args != None):
        call("java -classpath "+cp+" "+package[index]+" "+args.args,shell=True)
    else:
        call("java -classpath "+cp+" "+package[index],shell=True)

