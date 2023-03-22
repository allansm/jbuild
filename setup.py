from setuptools import setup, find_packages
import platform

setup(
    name="jbuild",
    version="2023.3.22",
    packages=find_packages(),

    install_requires=[],

    entry_points={
        'console_scripts': [
            'jbuild = allansm.jbuild.jbuild:main',
            'jrun = allansm.jbuild.jrun:main',
            'jcreate = allansm.jbuild.jcreate:main',
            'jcompile = allansm.jbuild.jcompile:main',
            'jexec = allansm.jbuild.jexec:main',
            'jjar = allansm.jbuild.jjar:main',
        ],
    }
)
