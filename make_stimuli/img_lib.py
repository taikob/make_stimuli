import cv2
import math as m
import scipy.stats as stats
import numpy as np

def ratesize(vs,vw,size):
    sr=m.tan(m.radians(float(vw)/2)) / m.tan(m.radians(float(vs)/2))  #size rate
    if size[0] > size[1]:
        cs=size[1] / 2#circle size
        ssize = (int(size[0] / 2 - cs), 0, int(size[0] / 2 + cs), size[1])  # stimuli size
        wsize = (int(size[0] / 2 - cs  * sr), int(cs - cs  * sr), int(size[0] / 2 + cs  * sr), int(cs + cs  * sr))  # stimuli size
    else:
        cs=size[0] / 2#circle size
        ssize = (0, int(size[1] / 2 - cs), size[0], int(size[1] / 2 + cs))  # stimuli size
        wsize = (int(cs - cs * sr), int(size[1] / 2 - cs  * sr), int(cs + cs  * sr), int(size[1] / 2 + cs  * sr))  # stimuli size
    return ssize, wsize

def scale_box(img, width, height):
    h, w = img.shape[:2]
    rd = w - (w * height)/width

    img1 = img[int(rd/2): w-int(rd/2),0 : h]
    img1 = cv2.resize(img1, dsize=(width, height))

    return img1

def make_square(img,sw=[0,0,0]):
    size=img.shape
    if size[0]!=size[1]:
        if size[0]>size[1]:
            ptc = [0, int((size[0]-size[1])/2)-1]
            tmp = size[0]
        else:
            ptc = [int((size[1]-size[0])/2)-1, 0]
            tmp = size[1]
        newimg = np.zeros((tmp, tmp, 3))
        if isinstance(sw,list):#set background RGB
            rgb=sw
        elif sw==1: #average color
            rgb=[np.mean(img[:,:,0]),np.mean(img[:,:,1]),np.mean(img[:,:,2])]
        elif sw==2: #mode
            rgb=[stats.mode(np.ravel(img[:,:,0]))[0],\
                 stats.mode(np.ravel(img[:,:,1]))[0],\
                 stats.mode(np.ravel(img[:,:,2]))[0]]
        newimg[:,:,0]=rgb[0]
        newimg[:,:,1]=rgb[1]
        newimg[:,:,2]=rgb[2]
        newimg[ptc[0]:ptc[0]+size[0], ptc[1]:ptc[1]+size[1]] = img
    else:
        newimg=img
    return newimg