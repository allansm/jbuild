def include(path):
    import sys
    import os
    from os.path import dirname,realpath
    from glob import glob
    
    tmp = os.getcwd()
    os.chdir(dirname(realpath(__file__)))

    anyFile = glob(path+"/*")[0]
    path = dirname(realpath(anyFile))

    sys.path.append(path)

    os.chdir(tmp)

include("../python-lib")
