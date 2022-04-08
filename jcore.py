from os.path import exists
from os import remove

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
