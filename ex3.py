import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
(b, g, r) = image[cY, cX]

print(f"Pixel at middle point: ({cX}, {cY}) - "
      f"Red: {r}, Green: {g}, Blue: {b}")

cv2.waitKey(0)