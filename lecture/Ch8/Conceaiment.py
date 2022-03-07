from cs1media import *
import math

pict1 = load_picture("C:/Users/82102/Pictures/izone.jpg")
pict2 = load_picture("C:/Users/82102/Pictures/dog.jpg")


print("pict1 size %d %d " % pict1.size())
print("pict2 size %d %d " % pict2.size())


def make_even(color):
    r, g, b = color
    r -= r % 2
    g -= g % 2
    b -= b % 2
    return (r, g, b)

def make_even_img(img):
    w, h = img.size()
    for x in range(w):
        for y in range(h):
            img.set(x, y, make_even(img.get(x,y)))

def Concealment(img1, img2):
    make_even_img(img1)
    w, h = img2.size()
    for x in range(w):
        for y in range(h):
            if is_black(img2.get(x, y)):
                r, g, b = img1.get(x, y)
                r -= 1
                img1.set(x,y, (r, g, b))
    return img1


def red_1(img, x, y):
    r, g, b = img.get(x, y)


def is_black(color):
    r, g, b = color
    if math.sqrt(r**2 + r**2 + b**2 ) < 50:
        return True
    else:
        return False


def decode(img):
    w, h = img.size()
    for x in range(w):
        for y in range(h):
            r, g, b = img.get(x, y)
            if r%2 == 1:
                img.set(x, y, (64, 255, 255))

    img.show()

pict1.show()
pict2.show()
conceal = Concealment(pict1, pict2)
conceal.show()
decode(conceal)



