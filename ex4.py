import cv2
import imutils

image = cv2.imread('image.jpg')
methods = (cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4)
for x in range(len(methods)):
    resized = imutils.resize(image, height=image.shape[0]*3, inter=methods[x])
    cv2.imshow(f'image{x}', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()