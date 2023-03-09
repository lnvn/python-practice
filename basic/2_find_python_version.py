import os
import platform

def get_python_version1():
    pyversion = os.sys.version
    print("Current version: ",pyversion)

def get_python_version2():
    pyversion = platform.python_version()
    print("Current version: ",pyversion)


get_python_version1()
get_python_version2()