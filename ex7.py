import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

p_width = w // 3
p_height = h // 3

start_x = p_width
start_y = p_height
end_x = p_width * 2
end_y = p_height * 2

middle_part = image[start_y:end_y, start_x:end_x]

cv2.line(image, (p_width, 0), (p_width, h), (0, 0, 0), 1)
cv2.line(image, (p_width * 2, 0), (p_width * 2, h), (0, 0, 0), 1)

cv2.line(image, (0, p_height), (w, p_height), (0, 0, 0), 1)
cv2.line(image, (0, p_height * 2), (w, p_height * 2), (0, 0, 0), 1)

cv2.imshow("9 slices", image)

cv2.imshow("Middle cutted", middle_part)

cv2.waitKey(0)