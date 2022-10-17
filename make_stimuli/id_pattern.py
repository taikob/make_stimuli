from color import convert as c
import math as m

def FW_dist(cn, H1,H2=0,calib=0, monodata=None):
    if cn==3:#color number
        return [(0,0,0), cc(H1,calib=calib, monodata=monodata), (255,255,255)]
    elif cn==4:
        return [(0,0,0), cc(H1,calib=calib, monodata=monodata), (255,255,255), cc(H2, calib=calib, monodata=monodata)]#[(0,0,0), (100, 120, 255), (255,255,255), (220, 235, 0)]
    else:
        print('nc must be 3 or 4')

def cc(H,calib=0, monodata=None):#colorcode

    if monodata is None:
        rRGB = c.HLS_to_RGB(H, 0.5, 1)
        if calib==0: return [int(rRGB[0]*255),int(rRGB[1]*255),int(rRGB[2]*255)]
        elif calib==1: return c.get_fixRGB([rRGB[0]*255,rRGB[1]*255,rRGB[2]*255])
    else:
        di=int(monodata[int(float(H)/10.0)][1])
        return [di,di,di]

def envsin(amp, num, f1, f2=None, p=None):
    ld=[]
    da=2*m.pi/float(num)
    amp=amp*127.5
    if f2 is not None:
        ph1 = 0; ph2 = float(num*float(p)/1000)
    else:
        ph1 = float(num*float(p)/1000); ph2 = 0
    angl = 0
    for n in range(num):
        l = amp * m.sin(angl * f1 + da * ph1)
        if f2 is not None: l *= 0.5 * m.sin(angl * f2 + da * ph2) + 0.5
        l = int(l+127.5)
        ld.append((l,l,l))
        angl+=da
    return ld