import pafy
import cv2

url = 'https://youtu.be/wRYCqpaV1iY'
urlPafy = pafy.new(url)
videoplay = urlPafy.getbest()
print (urlPafy)


cap = cv2.VideoCapture(videoplay.url)
while (True):
    ret,src = cap.read()
    cv2.imshow('src',src)
    #do your stuff here.

cap.release()
cv2.destroyAllWindows()
