import cv2
import imutils

x = int(input('Vertical move: '))
y = int(input('Horizontal move: '))

img = cv2.imread('image.jpg')
shifted = imutils.translate(img,x,y)
cv2.imshow('shifted', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()