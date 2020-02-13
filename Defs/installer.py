import os

def pip(req) :
    os.system("pip3 install %s" % req)
