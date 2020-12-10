import os
import shutil
import util as u
frame_number=20
imagepath='.'
mncr=1

def make_stimulus_dir(image, folder, image_num):
    os.makedirs(folder)
    with open(folder + '/read_list.txt', mode='w') as f:
        for n in range(image_num):
            copy = folder + '/' + str(n) + '.jpg'
            shutil.copyfile(image, copy)
            f.write(folder + '/' + str(n) + '.jpg\n')

for dir in os.listdir(imagepath):
    if '.jpg' in dir or '.png' in dir:
        if '.png' in dir:
            u.pngtojpg(dir)
            dir=dir.replace('.png','.jpg')
        u.resize(dir, dir, [120,160])
        if mncr==1: u.trans_mncr(dir)
        make_stimulus_dir(dir, dir.replace('.jpg',''), frame_number)