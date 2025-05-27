import cv2

image = cv2.imread('image.jpg')
resized = cv2.resize(image, (image.shape[0]*2, image.shape[1]*2), interpolation=cv2.INTER_LINEAR)

cv2.imshow('image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()