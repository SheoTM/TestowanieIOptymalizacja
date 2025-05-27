import cv2
import imutils

image = cv2.imread("image.jpg")
resized_save = imutils.resize(image, width=800)
cv2.imwrite("resized_output.jpg", resized_save)
cv2.imshow("Saved", resized_save)
cv2.waitKey(0)
cv2.destroyAllWindows()
