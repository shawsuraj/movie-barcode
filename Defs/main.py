#!/usr/bin/python3
import argparse
import os
import cv2 as cv
import time
from tqdm import tqdm
import pafy
import sys
import re
import shutil
# from multiprocessing import Pool

# sys.path.append('/usr/local/lib/python3.7/site-packages')

parser = argparse.ArgumentParser(description = 'Video Clip to barcode form...')
parser.add_argument('-f','--file',
                    metavar = 'abc.mp4',
                    help = "Location of the video file")
parser.add_argument('-u', '--url',
                    metavar = "https://youtu.be/xyz",
                    help = "Url of the video")
parser.add_argument('-b', '--bar',
                    action="store_true",
                    help="Create barcode of the video")
parser.add_argument('-s', '--save',
                    action="store_true",
                    help = "Save all the frames of a video")
parser.add_argument('-t', '--time',
                    metavar = 'hhmmss-hhmmss',
                    help = "Capture from a specific time. format => hh:mm:ss-hh:mm:ss")
parser.add_argument('-v', '--verbose',
                    action="store_true",
                    help = "Show progress")

args = parser.parse_args()

# Setup the dir
def dirSetup(vid) :
    if args.file :
        dir = os.path.basename(args.file)     #Setting up folder
        dir = os.path.splitext(dir)[0]
    elif args.url :
        dir = vid.title

    if not os.path.exists(dir) :
        os.mkdir(dir)
        return os.getcwd() + '/' + dir
    else :                           #Error handling if folder exists
        i = 0
        dir = dir + '-'+str(i)
        while True :
            if not os.path.exists(dir) :
                os.mkdir(dir)
                return os.getcwd() + '/' + dir
            else :
                j = (i/10) + 1
                i += 1
                dir = dir[0:-int(j)] + str(i)

# Initialing info of vid to make same format for different sources
def readVideo() :
    if args.file :
        vid = args.file
        vidCap = cv.VideoCapture(vid)
    elif args.url :
        vid = pafy.new(args.url)
        videoplay = vid.getbestvideo(preftype="any",ftypestrict=True)
        vidCap = cv.VideoCapture(videoplay.url)
    else :
        print("No file or url provided..")

    return vidCap

# Main working of frame capture processing
def framecap(vidCap, frameCounts, dir) :
    startFrameCount, endFrameCount, totalFrameCount = map(int, frameCounts)
    # print(startFrameCount, endFrameCount, totalFrameCount)
    vidCap.set(1,startFrameCount)
    image = vidCap.read()[1]

    if args.verbose :
        pbar = tqdm(total=endFrameCount - startFrameCount, desc = "Processing", unit = "frames")

    for currFrameCount in range(startFrameCount, endFrameCount) :                #All frames
    # while success :
    # for i in range(5000):     #Limited frames
        try :
            if args.save :
                cv.imwrite(os.path.join(dir, "frame%d.jpg" % currFrameCount), image)     # save frame as JPEG filee

            if args.bar :
                # createBar(image, count, len, dir)
                if currFrameCount == startFrameCount :
                    bar = resize(image, dir)
                elif currFrameCount < (endFrameCount - 1) :
                    bar = concat(bar ,resize(image, dir))
                else :
                    bar = concat(bar ,resize(image, dir))
                    cv.imwrite("%sbar.jpg" % dir, bar)

        except AttributeError:
            print("\nSkipping Frame %d -> AttributeError" % currFrameCount)

        image = vidCap.read()[1]
        currFrameCount += 1

        if 'pbar' in locals():      # Progress bar update
            pbar.update(1)

    if 'pbar' in locals():
        pbar.close()

# Create barcode.. resize width : 1px
def createBar(image, count, len, dir) :
    if count == 0 :
        bar = resize(image, dir)

    elif count < (len - 1) :
        bar = concat(bar ,resize(image, dir))

    else :
        bar = concat(bar ,resize(image, dir))
        cv.imwrite("%sbar.jpg" % dir, bar)

# Resize frame : SI rule followed
def resize(image, dir):
    width = 1               # Each frame's width
    height = image.shape[0] # keep original height
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return resized

# Concatenate the img
def concat(bar, resized):
    return cv.hconcat([bar, resized])

def endmessage(dir) :
    print("[*] All the files are saved in >> " + dir)

# Custom time vid cap
def samay(vidCap) :
    totalFrameCount = int(vidCap.get(cv.CAP_PROP_FRAME_COUNT))  # total frames

    if args.time :
        # time input format : hh:mm:ss-hh:mm:ss
        stime, etime = map(str,args.time.split('-'))

        # check time format
        if not isTimeFormat(stime) or not isTimeFormat(etime) :
            print("Use correct time format (start-end) >> hh:mm:ss-hh:mm:ss")
            print("Exiting....!!!")
            remSaboot(dir)
            time.sleep(2)
            sys.exit()
    else :
        return 0, totalFrameCount, totalFrameCount  # cap all if no time specified

    fps = int(vidCap.get(cv.CAP_PROP_FPS))

    # Convert everything to seconds and then get frame numbers
    stime = list(map(int, stime.split(':')))
    startFrameCount = sum([(60 ** i) * stime[2-i] for i in range(3)]) * fps  # starting frame count

    etime = list(map(int, etime.split(':')))
    endFrameCount = sum([(60 ** i) * etime[2-i] for i in range(3)]) * fps    # last frame count

    if not endFrameCount :  # Capture till last if 00:00:00 specified at end
        endFrameCount = totalFrameCount

    return startFrameCount, endFrameCount, totalFrameCount

# Check time format
def isTimeFormat(test_time) :
    regex = r"^\d{2}:\d{2}:\d{2}$"   # hh:mm:ss

    return bool(re.match(regex, test_time, re.MULTILINE))

# Remove processed files if exception occurs
def remSaboot(dir) :
    if os.path.exists(dir) :
        shutil.rmtree('{}'.format(dir))
