#!/usr/bin/python3

import argparse
import os
import cv2 as cv
import numpy as np
import time

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-v', help = "location of the video file")

args = parser.parse_args()

def framecap(file) :
    vidCap = cv.VideoCapture(file)
    success,image = vidCap.read()
    success = True
    while True :          #All frames
    # for i in range(5000):   #Limited frames
        resize(image)
        success,image = vidCap.read()

def resize(image):
    width = 1 #Each frame's width
    height = image.shape[0] # keep original height
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    if not os.path.isfile("bar.jpg") :
        cv.imwrite("bar.jpg", resized)
    else :
        bar(resized)

def bar(resized):
    bar = cv.imread('bar.jpg')
    im_h = cv.hconcat([bar, resized])
    os.remove('bar.jpg')
    cv.imwrite('bar.jpg', im_h)



if __name__ == "__main__" :
    try :
        if os.path.isfile('bar.jpg') :
            os.remove('bar,jpg')
        vid = args.v
        framecap(vid)

    except KeyboardInterrupt :
        print("Exiting....!!!")
        time.sleep(2)
