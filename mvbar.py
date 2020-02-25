#!/usr/bin/python3
#
#@shawsuraj

import sys
import time

try :
    from Defs.main import start

except ImportError :
    from Defs.checks import check, install
    check()
    install()

    from Defs.main import start

if __name__ == "__main__" :
    try :
        start()

    except KeyboardInterrupt :
        print("\nExiting....!!!")
        time.sleep(2)
