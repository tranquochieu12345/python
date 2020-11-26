import numpy as np
import cv2


img = cv2.imread('dog.jpg',0)

cv2.imshow('quang',img)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'ai day ?',(10,200), font, 2,(100,24,50),4,cv2.LINE_AA)

cv2.imshow('hieu',img)
cv2.waitKey(0)