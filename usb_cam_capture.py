#-*- coding: utf-8 -*-
import cv2
import numpy as np
import imutils
from datetime import datetime
import time

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



cap = cv2.VideoCapture(0)  
if cap.isOpened() == False:
    print('카메라를 오픈 할 수 없습니다.')

#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#out = cv2.VideoWriter('output.avi', fourcc, 25.0, (frame_width,frame_height))


frame_width = int(3840)
frame_height = int(2160)

MJPG_CODEC = 1196444237.0 # MJPG

cv2.namedWindow('Usb Cam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Usb Cam', frame_width,frame_height)

bightness = cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)
cap.set(cv2.CAP_PROP_FOURCC, MJPG_CODEC)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
#print cap.get(cv2.CAP_PROP_BRIGHTNESS)
print cap.get(cv2.CAP_PROP_FOURCC)

while True:
	ret, frame = cap.read()

	#change to frame size 
        #frame = cv2.resize(frame, (frame_width, frame_height))
	# rotate_frame = imutils.rotate(frame, 0) 
	#frame = Rotate(frame, 90)
	cv2.imshow('Usb Cam', frame)
        #out.write(frame)	

	ch = cv2.waitKey(1)
	if ch == ord('q'):
	    break

	elif ch == ord('c'):
	    print('press c')
	    cv2.imwrite('./saved_images/usbcam({}).jpg'.format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')),frame)
	    print('./saved_images/usbcam({}).jpg saved'.format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')))


	elif ch == ord('s'):
		for i in range(2):
		    cv2.imwrite('./saved_images/usbcam({})_{}.jpg'.format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),i),frame)
		    print('./saved_images/usbcam({})_{}.jpg saved'.format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),i))
		    time.sleep(1)



#out.release()
cap.release()
#cap1.release()
cv2.destroyAllWindows()
