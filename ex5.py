import cv2

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
x_start = w // 2
x_end = w
y_start = 0
y_end = h
fragment = image[y_start:y_end, x_start:x_end]
flipped_fragment = cv2.flip(fragment, 1)
image[y_start:y_end, x_start:x_end] = flipped_fragment
cv2.imshow("Flipped", image)
cv2.waitKey(0)
cv2.destroyAllWindows()