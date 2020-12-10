import cv2
import os
import sys
import numpy as np

#input parameter
width=160
height=120
monochrome=0
videopath='training_data.mp4'

vidcap = cv2.VideoCapture(videopath)
success, image = vidcap.read()
count = 0
files = []
print("Start to save images...")

videofolder=videopath.replace('.mp4','')
os.makedirs(videofolder)  # made models

while True:
    success, image = vidcap.read()
    if not success:
        break
    files.append(os.path.join(videofolder, "frame_%05d.jpg" % (count)))
    sys.stdout.write('\rSave {}'.format(files[-1]))
    sys.stdout.flush()
    image = cv2.resize(image, (width, height))
    if monochrome==1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(files[-1], image)
    count += 1


read_list_file = os.path.join(videofolder, "read_list.txt")

print('\nSave %s' % read_list_file)
with open(read_list_file, 'w') as f:
    f.write('\n'.join(files))

print("Done.")
