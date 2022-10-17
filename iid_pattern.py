import random
import numpy as np

def random01():
    return random.randint(0, 1)

def RD(dts, ims):
    #dts: dot size
    #ims: image size
    dms=(int(ims[0]/dts[0]), int(ims[1]/dts[1])) #dot map size
    im = np.array(list(map(random01, np.empty(dms[0] * dms[1]))), np.uint8)*255

    im = im.reshape(dms[0], dms[1])
    im= im.repeat(dts[0], axis=0).repeat(dts[1], axis=1)

    return im