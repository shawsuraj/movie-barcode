#!/usr/bin/python3

import argparse
import os
import cv2 as cv
import numpy as np
import time


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-v', help = "location of the video file")

args = parser.parse_args()

# if args.v:
#     print("file : " + args.v)

def baseSetup(file) :
    dir = os.path.basename(file)
    dest_dir = os.path.splitext(dir)[0]
    #Creating new folder with filename
    if not os.path.exists(dest_dir) :
        os.mkdir(dest_dir)
        return dest_dir
    else :         #Error handling if folder exists
        i = 0
        dest_dir = dest_dir + '('+str(i)+')'
        while True :
            if not os.path.exists(dest_dir) :
                os.mkdir(dest_dir)
                return dest_dir
            else :
                i += 1
                dest_dir = dest_dir[0:-2] + str(i) + dest_dir[-1:]

def framecap(file,dir) :
    vidCap = cv.VideoCapture(file)
    success,image = vidCap.read()
    # count = 0
    success = True
    # length = int(vidCap.get(cv.CAP_PROP_FRAME_COUNT))
    print(length)

    while success:
        # cv.imwrite(os.path.join(dir, "frame%d.jpg" % count), image)     # save frame as JPEG file
        barcode(dir, image, count)
        success,image = vidCap.read()
        count += 1

def resize(dir, image):
    width = 1
    height = image.shape[0] # keep original height
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    if not os.path.isfile(dir/bar.jpg) :
        cv.imwrite(os.path.join(dir, "bar.jpg"), resized)
    else :
        bar(resized)
    # cv.imwrite(os.path.join(dir, "frame%d.jpg" % count), resized)

def bar:
    im_h = cv2.hconcat([, im1])


if __name__ == "__main__" :
    try :
        vid = args.v
        dir = baseSetup(vid)
        framecap(vid, dir)

    except KeyboardInterrupt :
        print("Exiting....!!!")
        time.sleep(2)
