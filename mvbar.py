#!/usr/bin/python3
#
#v002
#
#shawsuraj

import argparse
import os
import cv2 as cv
import time
from tqdm import tqdm

parser = argparse.ArgumentParser(description = 'Video Clip to barcode form...')
parser.add_argument('file', metavar = 'abc.mp4', help = "Location of the video file")
parser.add_argument('-s', '--save', action="store_true", help = "Save all the frames of a video")
parser.add_argument('-v', '--verbose', action="store_true", help = "Show progress")

args = parser.parse_args()

def baseSetup(vid) :
    #Setting up folder
    dir = os.path.basename(vid)
    dir = os.path.splitext(dir)[0]
    #Creating new folder with filename
    if not os.path.exists(dir) :
        os.mkdir(dir)
        return os.getcwd() + '/' + dir
    else :         #Error handling if folder exists
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

def framecap(vid, dir) :
    vidCap = cv.VideoCapture(vid)
    success,image = vidCap.read()
    count = 0            #Initialise frame count
    success = True
    len = int(vidCap.get(cv.CAP_PROP_FRAME_COUNT))
    if args.verbose :
        pbar = tqdm(total=len, desc = "Processing", unit = "frames")
    for count in range(len) :                #All frames
    # while success :
    # for i in range(5000):     #Limited frames
        if args.save :
            # print(count)
            cv.imwrite(os.path.join(dir, "frame%d.jpg" % count), image)     # save frame as JPEG filee
        resize(image, dir)
        success,image = vidCap.read()
        count += 1
        if 'pbar' in locals():
            pbar.update(1)
    if 'pbar' in locals():
        pbar.close()

def resize(image, dir):
    width = 1               #Each frame's width
    height = image.shape[0] # keep original height
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    if not os.path.isfile("%sbar.jpg" % dir) :
        cv.imwrite("%sbar.jpg" % dir, resized)
    else :
        bar(resized, dir)

def bar(resized, dir):
    bar = cv.imread("%sbar.jpg" % dir)
    im_h = cv.hconcat([bar, resized])
    os.remove("%sbar.jpg" % dir)
    cv.imwrite("%sbar.jpg" % dir, im_h)

if __name__ == "__main__" :
    try :
        # if os.path.isfile('bar.jpg') :
        #     os.remove('bar,jpg')
        # print(args.save)
        vid = args.file
        dir = baseSetup(vid) + '/'
        # print(dir)
        framecap(vid, dir)

        print("All the files are saved in >> " + dir)

    except KeyboardInterrupt :
        print("\nExiting....!!!")
        time.sleep(2)
