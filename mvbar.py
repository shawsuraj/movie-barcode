#!/usr/bin/python3

import argparse
import os
import cv2 as cv
import numpy as np
import time

parser = argparse.ArgumentParser(description = 'Video Clip to barcode form...')
parser.add_argument('file', metavar = 'abc.mp4', help = "Location of the video file")
parser.add_argument('-s', '--save', action="store_true", help = "Save all the frames of a video")
# parser.add_argument('-v', '--verbose', action="store_true", help = "Width of each frame")

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

def framecap(vid, dir, save_frame = False) :
    vidCap = cv.VideoCapture(vid)
    success,image = vidCap.read()
    count = 0
    success = True
    # length = int(vidCap.get(cv.CAP_PROP_FRAME_COUNT))
    while True :          #All frames
    # for i in range(5000):   #Limited frames
        if save_frame :
            cv.imwrite(os.path.join(dir, "frame%d.jpg" % count), image)     # save frame as JPEG filee
            count += 1
        resize(image, dir)
        success,image = vidCap.read()

def resize(image, dir):
    width = 1 #Each frame's width
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
        framecap(vid, dir, args.save)

        print("All the files are saved in >> " + dir)

    except KeyboardInterrupt :
        print("\nExiting....!!!")
        time.sleep(2)
