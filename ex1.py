import cv2
import numpy as np

img = cv2.imread('image.jpg')
M = np.float32([[1,0,30],[0,1,40]])
shifted = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
cv2.imshow('shifted', shifted)
cv2.waitKey(0)