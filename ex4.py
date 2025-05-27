import cv2
import imutils
#Nie widzę różnicy ?
img = cv2.imread('image.jpg')
shifted = imutils.translate(img,100,50)
cv2.imshow('shifted', shifted)
cv2.waitKey(0)
