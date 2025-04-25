import cv2

image = cv2.imread("image.jpg")
if image is not None:
    (h, w, c) = image.shape
    print(f'width: {w}px, height: {h}px, channels: {c}')
else:
    print("Error.")
