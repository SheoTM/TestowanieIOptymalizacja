import cv2
image = cv2.imread('person.jpg')
# height, width = image.shape[:2]
# center_x = width // 2
# center_y = height // 2
# print(f"W: {width}, H: {height}")
# print(f"M: ({center_x}, {center_y})")

red = (0, 0, 255)
cv2.circle(image, (500, 360), 20, red, -1)
cv2.circle(image, (680, 360), 20, red, -1)

green = (0, 255, 0)
cv2.rectangle(image, (630, 560), (530, 510), green, -1)

blue = (255, 0, 0)
cv2.circle(image, (600, 400), 240, blue, 2)

cv2.imshow("Face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()