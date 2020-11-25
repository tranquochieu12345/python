import numpy as np
import cv2
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

img = cv2.imread("dog.jpg",0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()