from PIL import Image, ImageDraw

def make_circle(dist,size,ssize,wsize,trn,bg):

    da = float(360) / float(trn*len(dist))  # d angle
    im = Image.new('RGB', size, (bg,bg,bg))
    draw = ImageDraw.Draw(im)
    d=0
    for t in range(trn):
        for RGB in dist:
            draw.pieslice(ssize, start=d-da, end=d, fill=tuple(RGB), outline=tuple(RGB))
            d+=da

    draw.ellipse(wsize, fill=(bg, bg, bg), outline=(bg, bg, bg))

    return im, Image.new('RGB', size, (bg,bg,bg))