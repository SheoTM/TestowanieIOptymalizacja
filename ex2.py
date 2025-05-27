import cv2
import numpy as np

blackscreen = np.zeros((400, 400, 3))
green = (0, 255, 0)
cv2.rectangle(blackscreen, (0, 0), (100, 50), green, -1)
red = (0, 0, 255)
cv2.rectangle(blackscreen, (300, 350), (400, 400), red, 3)
cv2.imshow("Rectangles", blackscreen)
cv2.waitKey(0)
cv2.destroyAllWindows()