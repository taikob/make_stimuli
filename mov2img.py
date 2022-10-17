import os, cv2
from data_prcs import get as g
import img_lib as il

def mov2img(file,root, size=None, stp=None):
    vidcap = cv2.VideoCapture(file)
    frmnum = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    count = -1; n=0; files = []

    dir = root + '/' + file.replace('.mp4','').replace('.MP4','').replace('.avi','').split('/')[-1]
    if not os.path.exists(dir): os.makedirs(dir)

    if stp is None:  stp = frmnum
    if stp > frmnum: stp = frmnum

    while stp > n:
        count += 1
        success, image = vidcap.read()
        if not success: print('can not read, frame No. is .. ', count); continue
        if size is not None: image=il.scale_box(image, size[0], size[1])
        cv2.imwrite(dir+'/'+"%05d.jpg"% (count), image)
        files.append(os.path.join(dir, "%05d.jpg" % (count)))
        n+=1

    read_list_file = os.path.join(dir, "read_list.txt")
    with open(read_list_file, 'w') as f: f.write('\n'.join(files))

    return n

def mov2stm(dir, stmdir, size, nmax=1e10):
    follist = g.get_folderlist(dir)
    if len(follist)==0:follist=[dir]
    follist = g.chk_havefilename(follist, '.mp4') + g.chk_havefilename(follist, '.MP4') + g.chk_havefilename(follist, '.avi')
    stmlist = []; n=0

    if not os.path.exists(stmdir): os.makedirs(stmdir)
    for fol in follist:
        root = fol.pop(0)
        if n >= nmax: break
        if len(fol)==0: continue
        for file in fol:
            print(root + '/' + file)
            n+= mov2img(root + '/' + file, stmdir, size=size, stp=int(nmax-n))
            stmlist.append(stmdir + '/' + file.replace('.mp4', '').replace('.MP4', '').replace('.avi', ''))

    with open(stmdir+'/seqfile.txt', 'w') as f: f.write('/read_list.txt\n'.join(stmlist))
    print('finish, total number of images is '+str(n))

if __name__ == '__main__':#for test
    file = 'f/g/GH010050.MP4'
    dir = 'test'
    size = [256,256]
    nmax = 100

    if os.path.isfile(file):
        mov2img(file,dir, size=size, stp=nmax)
    else:
        mov2stm(file, dir, size, nmax=nmax)