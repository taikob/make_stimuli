import cv2
import numpy as np
import os

#parameter
fps=10
tv=0.5
dadt=1
left=-298

dadttable=np.linspace(-5,5,11)

filetable=[]

#for Hf in range(0,360,30):
#    filetable.append('stimuli/Hf'+str(Hf)+'_O.jpg')
#    filetable.append('stimuli/Hf'+str(Hf)+'_M.jpg')

stimulipath='stimuli'
for d in os.listdir(stimulipath):
    if '.jpg' in d and not 'background.jpg' in d:
        filetable.append(stimulipath + '/' + d)

def make_movie(fps,tv,dadt,left,filet,dr):
    dadt=round(dadt, 1)
    top=0
    scale = 1.0
    da=float(dadt)/float(fps)
    nt=int(float(tv)*float(fps))

    back = cv2.imread('stimuli/background.jpg')
    img  = cv2.imread(filet)
    img_h = img.shape[0]
    img_w = img.shape[1]
    back_h = back.shape[0]
    back_w = back.shape[1]
    img_c = (int(img_w/2), int(img_h/2))
    back_c = (int(back_w/2), int(back_h/2))

    videotitle=dr+'/'+filet.replace('.jpg','').split('/')[-1]+'_a'+str(dadt)+'_l'+str(left)+'.mp4'
    video  = cv2.VideoWriter(videotitle, 0x00000020, fps, (back_w, back_h))

    angle=float(0)
    for t in range(nt):
        back2=back
        trans = cv2.getRotationMatrix2D(img_c, angle, scale)
        img2 = cv2.warpAffine(img, trans, (img_w,img_h), borderValue=(255, 255, 255), flags=cv2.INTER_CUBIC)

        back2[back_c[1]-img_h/2 +top:back_c[1]+img_h/2 + top, back_c[0]-img_w/2+left:back_c[0]+img_w/2 + left] = img2

        video.write(back2)
        angle+=da

    video.release()

for filet in filetable:
    if '.jpg' in filet:
        for dadt in dadttable:
            dr='movie/'+filet.replace('.jpg','').replace('_R-1','').replace('_R1','')
            if not os.path.exists(dr):
                os.makedirs(dr)
            print(filet,dr)
            make_movie(fps,tv,dadt,left,filet,dr)