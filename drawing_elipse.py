import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.imshow('hieu',img)

cv2.waitKey(0)