import dependency

from allansm.argsHandle import *
from subprocess import call
from allansm.fileHandle import *

args = getArgs(["cp","package","--args"])

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
