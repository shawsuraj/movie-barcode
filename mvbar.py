#!/usr/bin/python3
#
#@shawsuraj

import sys
import time

try :
    from Defs.main import *

except ImportError :
    from Defs.checks import check, install
    check()
    install()

    from Defs.main import start

if __name__ == "__main__" :
    try :
        if args.bar or args.save :
            vid = readVideo()
            dir = dirSetup(vid)
            framecap(vid, dir+ '/')
            endmessage(dir)

        else :
            print("No option provided..!!")
            sys.exit()


    except KeyboardInterrupt :
        print("\nExiting....!!!")
        time.sleep(2)
        sys.exit()
