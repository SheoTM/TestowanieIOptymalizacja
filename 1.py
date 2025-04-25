import cv2

image = cv2.imread("image.jpg")
if image is None:
    print("Cant load image")
else:
    print("Image loaded.")
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
