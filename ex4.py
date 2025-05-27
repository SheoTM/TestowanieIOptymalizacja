import cv2

image = cv2.imread('image.jpg')
cv2.imshow('image', image)
flipped = cv2.flip(image,  -1)
flipped2 = cv2.flip(image,  1)
flipped3 = cv2.flip(image,  0)
cv2.imshow("Flipped", flipped)
cv2.imshow("Flipped2", flipped2)
cv2.imshow("Flipped3", flipped3)
cv2.waitKey(0)