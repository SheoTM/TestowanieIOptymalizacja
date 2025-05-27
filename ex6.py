import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
centerx = w // 2
centery = h // 2

x1 = centerx - 50
y1 = centery - 50
x2 = centerx + 50
y2 = centery + 50


if x1 >= 0 and y1 >= 0 and x2 <= w and y2 <= h:
    image[y1:y2, x1:x2] = (0, 0, 255)

cv2.imshow("Changed", image)

cv2.waitKey(0)