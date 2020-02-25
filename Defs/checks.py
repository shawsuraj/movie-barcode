import sys

from Defs.installer import pip

def module_check(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def check() :
    global reqs
    reqs = {}
    req_f = open("requirements.txt")
    req = req_f.readline()[:-1]
    while req :
        if req == "opencv-python" :
            reqs["opencv-python"] = module_check("cv2")
        else :
            reqs[req] = module_check(req)
        req = req_f.readline()[:-1]
    # for req in reqs :
    #     module[req] = module_check[req]
    #
    # for req, installed in reqs.items() :
    #     installed = module_check(req)

def install() :
    for req, installed in reqs.items() :
        if not installed :
            pip(req)
