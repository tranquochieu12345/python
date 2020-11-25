import numpy as np
import cv2
# Load an color image in graysca
img = cv2.imread('dog.jpg',0)
# can resize window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# show image in box with the name is image
cv2.imshow('image',img)
# waits indefinitely for a key stroke.
cv2.waitKey(0)
# save the image
cv2.imwrite('doggray.png',img)

