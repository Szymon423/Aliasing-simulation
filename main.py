from PIL import Image
import PIL
import glob
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

# equation: f(x) = sin(n * x + m * pi/10), m = -M/2, ... , M/2, n = 3, 
# for M = 64


def genarateImage(path, M, _n):
    f = lambda x, n, m : np.sin(n * x + m * np.pi / 10.)

    X = np.linspace(0, 2*np.pi, 10000)
    Y = f(X, _n, M)

    plt.figure(figsize=(1, 1), dpi=256)
    plt.polar(X, Y)
    plt.grid(False)
    plt.box(False)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(path)
    plt.close()


# generate image sequence
# X = np.arange(-30, 30)
# i = 0
wings = 3
directoryPath = str(wings) + "n propeller\\"
# for x in X:
#     path = ""
#     if i < 10:
#         path = directoryPath + "0" + str(i) + ".png"
#     else:
#         path = directoryPath + str(i) + ".png"
#     genarateImage(path, x, wings)
#     i += 1



# Create the Gif
frames = []
imgs = [directoryPath + f for f in listdir(directoryPath) if isfile(join(directoryPath, f))]
# print(imgs)

# for i in imgs:
#     new_frame = Image.open(i)
#     frames.append(new_frame)

# frames[0].save(str(wings) + 'n.gif', format='GIF',
#                append_images=frames[1:],
#                save_all=True,
#                duration=50, loop=0)



# all images as 3D arrays in list 
imagesList = [np.array(Image.open(img)) for img in imgs]

source = imagesList[1].copy()
targetImage = imagesList[0]

print(targetImage.shape)

#for i in range(256):
targetImage[:][0:150][:] = source[:][0:150][:]

im_from_array = PIL.Image.fromarray(np.uint8(targetImage))
im_from_array.show()



