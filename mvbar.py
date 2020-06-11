#!/usr/bin/python3
#
#@shawsuraj

import sys
import time

try :
    sys.path.append('/usr/local/lib/python3.7/site-packages')
    from Defs.main import *

except ImportError :
    from Defs.checks import check, install
    check()
    install()

    from Defs.main import *

# class vid():
#     def __init__(self):
#         self.vid
#         self.dir
#
#     def getVideo(self, vid) :
#         self.vid = vid
#
#     def getDIR(self, dir) :
#         self.dir = dir


if __name__ == "__main__" :
    try :
        if args.bar or args.save :
            vid = readVideo()
            dir = dirSetup(vid)
            frameCounts = samay(vid)
            framecap(vid, frameCounts, dir+ '/')
            endmessage(dir)

        else :
            print("No option provided..!!")
            sys.exit()


    except KeyboardInterrupt :
        print("\nKeyboardInterrupt")
        print("Exiting....!!!")
        remSaboot(dir)
        time.sleep(2)
        sys.exit()

    except Exception as e :
        print("Exception :",e)
        print("Exiting....!!!")
        remSaboot(dir)
        time.sleep(2)
        sys.exit()





#  734/734 [00:10<00:00, 71.36frames/s]
