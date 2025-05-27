import cv2
image = cv2.imread('image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(min_val, max_val, min_cord, max_cord) = cv2.minMaxLoc(gray_image)
print(f"Brightest pixel: {max_val}")
print(f"Coordinates of the brightest pixel: {max_cord}")
image[50:100, 50:100] = (255, 255, 255)