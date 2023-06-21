import numpy as np
from PIL import Image
from math import *

image = Image.open("cameraman.tif")

intense = np.array(image)
intense1 = np.array(image)
intense2 = np.array(image)
intense3 = np.array(image)
intense4 = np.array(image)

#image.show()

def Sobel3x3(i, j, inten):
    x1 = inten[i-1][j-1]
    x2 = inten[i-1][j]
    x3 = inten[i-1][j+1]
    x4 = inten[i][j-1]
#    x5 = inten[i][j]
    x6 = inten[i][j+1]
    x7 = inten[i+1][j-1]
    x8 = inten[i+1][j]
    x9 = inten[i+1][j+1]
    G_x = x7 + 2*x8 + x9 - (x1 + 2*x2 + x3)
    G_y = x3 + 2*x6 + x9 - (x1 + 2*x4 + x7)
    return sqrt(G_x**2 + G_y**2)


for i in range(1, int(len(intense))-1):
    for j in range(1, int(len(intense[0])) - 1):
        intense1[i][j] = Sobel3x3(i, j, intense)

#img = Image.fromarray(intense1)
#img.show()

def Sobel5x5(i, j):
    x1 = intense[i-2][j-2]
    x2 = intense[i-2][j-1]
    x3 = intense[i-2][j]
    x4 = intense[i-2][j+1]
    x5 = intense[i-2][j+2]
    x6 = intense[i-1][j-2]
    x7 = intense[i-1][j-1]
    x8 = intense[i-1][j]
    x9 = intense[i-1][j+1]
    x10 = intense[i-1][j+2]
    x11 = intense[i][j-2]
    x12 = intense[i][j-1]
    x14 = intense[i][j+1]
    x15 = intense[i][j+2]
    x16 = intense[i+1][j-2]
    x17 = intense[i+1][j-1]
    x18 = intense[i+1][j]
    x19 = intense[i+1][j+1]
    x20 = intense[i+1][j+2]
    x21 = intense[i+2][j-2]
    x22 = intense[i+2][j-1]
    x23 = intense[i+2][j]
    x24 = intense[i+2][j+1]
    x25 = intense[i+2][j+2]
    G_x = x1/4 + x2/2 + x3 + x4/2 + x5/4 + x6/2 + x7 + 2*x8 + x9 + x10/2 - (x16/2 + x17 + 2*x18 + x19 + x20/2 + x21/4 + x22/2 + x23 + x24/2 + x25/4)
    G_y = x5/4 + x10/2 + x15 + x20/2 + x25/4 + x4/2 + x9 + 2*x14 + x19 + x24 - (x2/2 + x7 + 2*x12 + x17 + x22/2 + x1/4 + x6/2 + x11 + x16/2 + x21/4)
    return sqrt(G_x**2 + G_y**2)


for i in range(2, int(len(intense))-2):
    for j in range(2, int(len(intense[0])) - 2):
        intense2[i][j] = Sobel5x5(i, j)


#img1 = Image.fromarray(intense2)
#img1.show()

def prepar(i, j, minimum, maximum, k, b):
    imges = 0
    if minimum <= intense[i][j] <= maximum:
        imges = k * intense[i][j] + b
    return imges

for i in range(int(len(intense))):
    for j in range(int(len(intense[0]))):
        intense3[i][j] = prepar(i, j, 100, 200, 1, 0)

#img2 = Image.fromarray(intense3)
#img2.show()

for i in range(1, int(len(intense)) - 1):
    for j in range(1, int(len(intense[0]))-1):
        intense4[i][j] = Sobel3x3(i, j, intense3)

img3 = Image.fromarray(intense4)
img3.show()