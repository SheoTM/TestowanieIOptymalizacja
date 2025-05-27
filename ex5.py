import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
centerx = w // 2
centery = h // 2
image[0:centery, 0:centerx] = (255,0,0)
cv2.imshow("Changed", image)

cv2.waitKey(0)