import cv2

def resize(originalpath, savepath, size):
    img = cv2.imread(originalpath)
    img2 = cv2.resize(img , (size[1], size[0]))
    cv2.imwrite(savepath, img2)

def trans_mncr(path):
    img = cv2.imread(path)
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, im_gray)


def pngtojpg(path):
    img = cv2.imread(path)
    cv2.imwrite(path.replace('.png','.jpg'), img)
