from jcore import *
from subprocess import call
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("cp")
parser.add_argument("package")
parser.add_argument("--args", required=False)

args = parser.parse_args()

args.cp = args.cp.replace("\\","/")

cp = "\""+args.cp+"/bin;"+args.cp+"/lib;"

if(exists(args.cp+"/.lib")):
    for x in getLines(args.cp+"/.lib"):
        cp+=";"+x
 
cp+="\""

if(args.args != None):
    call("java -cp "+cp+" "+args.package+" "+args.args)
else:
    call("java -cp "+cp+" "+args.package)
