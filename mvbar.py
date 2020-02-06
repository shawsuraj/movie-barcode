#!/usr/bin/python3
#
#@shawsuraj
#
#v003

import sys
try:
    from Defs.main import *
except ImportError:
    from Defs.checks import *
    check()
    sys.exit()

if __name__ == "__main__" :
    try :
        start()

    except KeyboardInterrupt :
        print("\nExiting....!!!")
        time.sleep(2)
