import cv2
image = cv2.imread('image.jpg')
original = image.copy()
image[100, :] = (0,255,0)
h,w=image.shape[:2]
print(f"Image size: {w} x {h}")
cv2.imshow("Original", original)
cv2.imshow("Changed", image)
cv2.waitKey(0)