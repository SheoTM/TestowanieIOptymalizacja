import cv2

gray_image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if gray_image is not None:
    cv2.imwrite("gray.jpg", gray_image)
    print("Saved as gray.jpg")
