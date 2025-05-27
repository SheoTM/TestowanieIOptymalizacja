import cv2
image = cv2.imread('image.jpg')
original = image.copy()
image[50:100, 50:100] = (255, 255, 255)
h,w=image.shape[:2]
cv2.imshow("Original", original)
cv2.imshow("Changed", image)
cv2.waitKey(0)