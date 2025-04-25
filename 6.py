import cv2

image = cv2.imread("image.jpg")
if image is not None:
    cv2.namedWindow("Scalable", cv2.WINDOW_NORMAL)
    cv2.imshow("Scalable", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()