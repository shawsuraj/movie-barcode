#!/usr/bin/python3
import argparse
import os
import cv2 as cv
import time
from tqdm import tqdm
import pafy

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
parser.add_argument('-v', '--verbose',
                    action="store_true",
                    help = "Show progress")

args = parser.parse_args()

def dirSetup(vid) :
    if args.file :
        dir = os.path.basename(vid)     #Setting up folder
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
                i += 1
                j = (i/10) + 1
                dir = dir[0:-int(j)] + str(i)

def readVideo() :
    try :
        if args.file :
            vid = args.file
        elif args.url :
            vid = pafy.new(args.url)
            # print (vid)
        return vid
    except :
        print("No file or url provided..")

def framecap(vid, dir) :
    if args.file :
        vidCap = cv.VideoCapture(vid)
    elif args.url :
        videoplay = vid.getbestvideo(preftype="any",ftypestrict=True)
        vidCap = cv.VideoCapture(videoplay.url)
    image = vidCap.read()[1]
    count = 0            #Initialise frame count
    len = int(vidCap.get(cv.CAP_PROP_FRAME_COUNT))
    if args.verbose :
        pbar = tqdm(total=len, desc = "Processing", unit = "frames")
    for count in range(len) :                #All frames
    # while success :
    # for i in range(5000):     #Limited frames
        try :
            if args.save :
                cv.imwrite(os.path.join(dir, "frame%d.jpg" % count), image)     # save frame as JPEG filee
            if args.bar :
                if count == 0 :
                    bar = resize(image, dir)
                elif count < (len - 1) :
                    bar = concat(bar ,resize(image, dir))
                else :
                    bar = concat(bar ,resize(image, dir))
                    cv.imwrite("%sbar.jpg" % dir, bar)
        except AttributeError:
            print("\nSkipping Frame %d -> AttributeError" % count)
        image = vidCap.read()[1]
        count += 1
        if 'pbar' in locals():      # Progress bar update
            pbar.update(1)
    if 'pbar' in locals():
        pbar.close()

def resize(image, dir):
    width = 1               #Each frame's width
    height = image.shape[0] # keep original height
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return resized

def concat(bar, resized):
    new_bar = cv.hconcat([bar, resized])
    return new_bar

def endmessage(dir) :
    print("[*] All the files are saved in >> " + dir)
