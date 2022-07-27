from os.path import exists, dirname

def writeFile(fn, data):
    f = open(fn, "w")
    f.write(data)
    f.close()

def readFile(fn):
    f = open(fn, "r")
    data = f.read()
    f.close()

    return data

def ls(path=".", ext="*"):
    from glob import glob

    return glob(path+"/"+ext)

def getLines(path):
    f = open(path, "r") 
    data = f.read().split("\n")
    f.close()

    return data

def getAllFiles(path,lamb=None):
    import os

    fold = os.walk(path)
    ret = []
    for root, dirs, files in fold:
        for name in files:
            if(lamb != None):
                lamb(os.path.join(root, name).replace("\\","/"))
            ret.append(os.path.join(root, name).replace("\\","/"))

    return ret

def isWindows():
    import platform

    if(platform.system() == "Windows"):
        return True
    
    return False

def mkdir(dir):
    from os import mkdir
    
    try:
        mkdir(dir)
    except:
        e=0

def remove(file):
    from os import remove
    
    try:
        remove(file)
    except:
        e=0

def classpath():
    import os
    
    if(os.getenv("CLASSPATH") == None):
        return ""
    
    return os.getenv("CLASSPATH")

