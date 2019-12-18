#-*- coding: utf-8 -*-
import cv2
import numpy as np
import imutils
from datetime import datetime
import time

iport = "243"

cap = cv2.VideoCapture("http://test@192.168.0." + iport + ":8090/?action=stream")

if cap.isOpened() :
    print('width : {}, height : {}'.format(cap.get(3), cap.get(4)))

cv2.namedWindow('{} Camera'.format(iport), cv2.WINDOW_NORMAL)
cv2.resizeWindow('{} Camera'.format(iport), 720, 1280)

bightness = cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)
print cap.get(cv2.CAP_PROP_BRIGHTNESS)

#change to fps
#raw = cv2.cv.CV_FOURCC(*'MJPG')
#out= cv2.VideoWriter('./Nobrand_Hand_man.avi', raw, 30.0, (1280, 720))

def Rotate(src, degrees) :
    if degrees == 90 :
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 1)

    elif degrees == 180 :
        dst = cv2.flip(src, 0)

    elif degrees == 270 :
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 0)

    else :
        dst = null

    return dst

while True:
    ret, frame = cap.read()

    #change to frame size 
    # frame = cv2.resize(frame, (1280, 720))
    # rotate_frame = imutils.rotate(frame, 0) 
    # out.write(resize)
    frame = Rotate(frame, 90)
    cv2.imshow('{} Camera'.format(iport), frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite('./saved_images/{}_camera({}).jpg'.format(iport, datetime.today().strftime('%Y.%m.%d-%H:%M:%S')),frame)
        print('./saved_images/{}_camera({}).jpg saved'.format(iport, datetime.today().strftime('%Y.%m.%d-%H:%M:%S')))


    if cv2.waitKey(1) & 0xFF == ord('s'):
        for i in range(10):
            cv2.imwrite('./saved_images/{}_camera({})_{}.jpg'.format(iport, datetime.today().strftime('%Y.%m.%d-%H:%M:%S'),i),frame)
	    print('./saved_images/{}_camera({})_{}.jpg saved'.format(iport, datetime.today().strftime('%Y.%m.%d-%H:%M:%S'),i))
	    time.sleep(2)



#out.release()
cap.release()
#cap1.release()
cv2.destroyAllWindows()