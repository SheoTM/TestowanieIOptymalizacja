import cv2

gray_image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if gray_image is not None:
    print(f'Gray image shape: {gray_image.shape}')
    print(f'channels: 1')
else:
    print("Error.")
