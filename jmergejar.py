from allansm import zip
from allansm.fileHandle import ls, remove, move
from os import chdir, mkdir, system, getcwd

print("extracting...\n")
for n in ls("."):
    print(n)
    zip.unzip(n, "tmp")

chdir("tmp")

dirs = ls(".")

mkdir("bin")

print("\nmoving...\n")
for n in dirs:
    print(n)
    move(n, "bin")

back = getcwd()

print("\ngenerating...\n")

import jjar

chdir(back)
mkdir("../output")
print("\nmoving...\n")
for n in ls("./", "*.jar"):
    print(n)
    move(n, "../output")

chdir("..")
remove("tmp")
