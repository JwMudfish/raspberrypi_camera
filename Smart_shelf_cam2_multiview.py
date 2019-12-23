#-*- coding: utf-8 -*-
import cv2
import numpy as np
from datetime import datetime
import time

cap1 = cv2.VideoCapture("http://test@192.168.0.240:8090/?action=stream")
cap2 = cv2.VideoCapture("http://test@192.168.0.242:8090/?action=stream")
cap3 = cv2.VideoCapture("http://test@192.168.0.243:8090/?action=stream")
cap4 = cv2.VideoCapture("http://test@192.168.0.243:8090/?action=stream")
cap5 = cv2.VideoCapture("http://test@192.168.0.245:8090/?action=stream")
cap6 = cv2.VideoCapture("http://test@192.168.0.246:8090/?action=stream")

def create_image_multiple(h, w, d, hcout, wcount):
    image = np.zeros((h*hcout, w*wcount,  d), np.uint8)
    color = tuple(reversed((0,0,0)))
    image[:] = color
    return image

def showMultiImage(dst, src, h, w, d, col, row):
    # 3 color
    if  d==3:
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w] = src[0:h, 0:w]
    # 1 color
    elif d==1:
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w, 0] = src[0:h, 0:w]
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w, 1] = src[0:h, 0:w]
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w, 2] = src[0:h, 0:w]

bightness = cap1.set(cv2.CAP_PROP_BRIGHTNESS, 100)
print (cap1.get(cv2.CAP_PROP_BRIGHTNESS))



red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
white = (255, 255, 255)


thickness = 2 

location = (200, 80)
#font = cv2.FONT_ITALIC  # italic font
#font = cv2.FONT_HERSHEY_SIMPLEX # normal size sans-serif font
font = cv2.FONT_ITALIC  # italic font
fontScale = 1

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
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()
    ret5, frame5 = cap5.read()
    ret6, frame6 = cap6.read()

    frame1 = Rotate(frame1, 90)
    frame2 = Rotate(frame2, 90)
    frame3 = Rotate(frame3, 90)
    frame4 = Rotate(frame4, 90)
    frame5 = Rotate(frame5, 90)
    frame6 = Rotate(frame6, 90)

    frame1 = cv2.resize(frame1, (480, 480))
    frame2 = cv2.resize(frame2, (480, 480))
    frame3 = cv2.resize(frame3, (480, 480))
    frame4 = cv2.resize(frame4, (480, 480))
    frame5 = cv2.resize(frame5, (480, 480))
    frame6 = cv2.resize(frame6, (480, 480))

    frame1 = cv2.putText(frame1, '240', location, font, fontScale, white, thickness)
    frame2 = cv2.putText(frame2, '241', location, font, fontScale, white, thickness)
    frame3 = cv2.putText(frame3, '243', location, font, fontScale, white, thickness)
    frame4 = cv2.putText(frame4, '243', location, font, fontScale, red, thickness)
    frame5 = cv2.putText(frame5, '245', location, font, fontScale, red, thickness)
    frame6 = cv2.putText(frame6, '246', location, font, fontScale, red, thickness)

    height = frame1.shape[0]
    width = frame1.shape[1]
    depth = frame1.shape[2]

    dstimage = create_image_multiple(height, width, depth, 2, 3)

    showMultiImage(dstimage, frame1, height, width, depth, 0, 0)
    showMultiImage(dstimage, frame2, height, width, depth, 0, 1)
    showMultiImage(dstimage, frame3, height, width, depth, 0, 2)
    showMultiImage(dstimage, frame4, height, width, depth, 1, 0)
    showMultiImage(dstimage, frame5, height, width, depth, 1, 1)
    showMultiImage(dstimage, frame6, height, width, depth, 1, 2)

    cv2.imshow('multiView',dstimage)

    ch = cv2.waitKey(1)
    if ch == ord('q'):
        break


