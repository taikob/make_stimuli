import cv2

#parameter
fps=10
tv=2
filename='stimuli/background.jpg'

videotitle=filename.replace('.jpg','.mp4').replace('stimuli/','')
nt=int(float(tv)*float(fps))

back = cv2.imread(filename)
back_h = back.shape[0]
back_w = back.shape[1]

video  = cv2.VideoWriter(videotitle, 0x00000020, fps, (back_w, back_h))

for t in range(nt):
    video.write(back)

video.release()