from ctypes import sizeof
from PIL import Image
from sys import argv
import random

# reading from file
filename = "text.txt"
txt = open(filename, "r")

# background photo to write on
bg = Image.open("Background/bg.png")
sheet_width = bg.width
gap, ht = 0, 0

last: str = ""

# for each character in text file, paste the corresponding letter from myfont1 or myfont2 onto output image
for i in txt.read().replace("\n", ""):
    if random.randint(0, 1) == 0:
        cases = Image.open("myfont1/{}.PNG".format(str(ord(i))))
    else:
        cases = Image.open("myfont2/{}.PNG".format(str(ord(i))))

    # if nearing the end of the page, write on new line
    if sheet_width < gap or len(i)*38 > (sheet_width-gap):
        gap, ht = 0, ht+100
        if last != "\n" or last != " ":
            if i.isalpha() == True:
                dash = Image.open("myfont1/45.png")
                bg.paste(dash, (gap, ht))
                gap += dash.width

    bg.paste(cases, (gap, ht))

    gap += cases.width

    last = i

# output image
bg.show()
