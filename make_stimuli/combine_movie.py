import cv2
import os
import random
import time
import shutil



def plus_movie(out, movie):
    plus=movie

    ret, frame = plus.read()

    i=0
    while ret:
        out.write(frame)
        ret, frame = plus.read()
        i+=1

    return out

def rand_ints_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns

def repeat_list(el,rp):
    ol=el[:]
    if rp>1:
        for r in range(rp-1):
            ol.extend(el)
    return ol

def combine_movie(flist,insertf,dir,numlist,nd):
    tm=str(int(time.time()))

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    #bgload
    bgmov = cv2.VideoCapture(insertf)

    #get movieinfo
    fps    = bgmov.get(cv2.CAP_PROP_FPS)
    height = bgmov.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = bgmov.get(cv2.CAP_PROP_FRAME_WIDTH)

    #make movie data
    nd=len(numlist)/nd
    ni=0
    nm=0 #number of movie
    while ni < len(numlist):

        print(nm)

        result = dir + '_' + tm + '_' + str(nm) + '.m4v'
        with open(result.replace('.m4v','.txt'), mode='w') as tt:
            out = cv2.VideoWriter(result, int(fourcc), fps, (int(width), int(height)))
            bgmov = cv2.VideoCapture(insertf)
            out = plus_movie(out, bgmov)
            while ni < nd*(nm+1):
                n = numlist[ni]
                f = flist[n]
                print(ni, f)
                movie = cv2.VideoCapture(dir+'/'+f)
                out = plus_movie(out,movie)
                bgmov = cv2.VideoCapture(insertf)
                out = plus_movie(out,bgmov)

                tt.write(f+'\n')
                ni+=1

            out.release()
            cv2.destroyAllWindows()

        shutil.copy(result.replace('.m4v','.txt'), result.replace('.m4v','_ans.txt'))

        nm+=1



filename=list()
for d in os.listdir('movie'):
    filename.append(d)

for fn in filename:
    if os.path.isdir('movie/'+fn):
        print(fn)
        dir='movie/'+fn
        flist=os.listdir(dir)
        flist = [f for f in flist if '.mp4' in f]
        insertf='movie/background.mp4'
        rp=20
        nd=5 #division number

        flist=repeat_list(flist,rp)

        numlist=rand_ints_nodup(0, len(flist)-1, len(flist))


        combine_movie(flist,insertf,dir,numlist,nd)