import cv2

image1 = cv2.imread("image.jpg")
image2 = cv2.imread("gray.jpg")

if image1 is not None and image2 is not None:
    cv2.imshow("Image 1", image1)
    cv2.imshow("Image 2", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
