import subprocess
import sys

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

def check() :
    modules = ['argparse','cv2','tqdm']
    not_installed = []
    for module in modules :
        if not module_exists(module) :
            not_installed.append(module)
    print("[*] Install %s module(s)" % not_installed[1:-1])
