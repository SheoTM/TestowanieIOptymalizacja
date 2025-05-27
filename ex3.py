import cv2

image = cv2.imread('image.jpg')
resized = cv2.resize(image, (200,300))

cv2.imshow('image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()