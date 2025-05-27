import cv2

image = cv2.imread("image.jpg")
print("Choose:")
print("0 – Vertical")
print("1 – Horizontal")
print("-1 – Vertically and horizontally")
flip_code = int(input("Give value: (0, 1, -1): "))
flipped_image = cv2.flip(image, flip_code)
cv2.imshow("Original", image)
cv2.imshow("Modified", flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
