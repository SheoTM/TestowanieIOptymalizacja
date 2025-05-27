import cv2
image = cv2.imread('image.jpg')
original = image.copy()

pixel_1 = image[50, 50]
pixel_2 = image[200, 200]
print(f"pixel value (50, 50): {pixel_1}")
print(f"pixel value (200, 200): {pixel_2}")
if (pixel_1 == pixel_2).all():
    print("Pixel values are the same.")
else:
    print("Pixel values are different.")