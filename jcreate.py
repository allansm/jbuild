from os import chdir
from os import mkdir
from os import getcwd
import allansm.argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument("name",type=str)

name = parser.parse_args().name

mkdir(name)

chdir(name)

mkdir("src")
mkdir("bin")

