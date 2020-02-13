#This program is to check an individual corrupt frame

import cv2 as cv
from sys import argv

count = 0

vid = argv[1]

vidCap = cv.VideoCapture(vid)

for count in range(30860) :
    success,image = vidCap.read()
    count += 1
    if count == 300 or count == 1200 or count == 2000 or count == 10000 or count == 25000 :

        print(count)

success,image = vidCap.read()

height, width, channels = image.shape
print (height, width, channels)
