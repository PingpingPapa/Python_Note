from cs1media import *
def luma(p):
    r, g, b = p
    return int(0.213 * r+ 0.715 * g+ 0.072 * b)

white = (255, 255, 255)
black = (0, 0, 0)

pict = load_picture("C:/Users/82102/Pictures/izone.jpg")

def blackwhite(img, threshold):
    w, h = img.size()
    for x in range(w):
        for y in range(h):
            if luma(img.get(x, y)) > threshold:
                img.set(x, y, white)
            else:
                img.set(x, y, black)

blackwhite(pict, 100)
pict.show()