import cv2
import numpy as np

blackscreen = np.zeros((300, 300, 3))
blue = (255, 0, 0)
cv2.circle(blackscreen, (50, 50), 40, blue, -1)
red = (0, 0, 255)
(centerX, centerY) = (blackscreen.shape[1] // 2,
                      blackscreen.shape[0] // 2)
cv2.circle(blackscreen, (centerX, centerY), 60, red, -1)
cv2.imshow("Circles", blackscreen)
cv2.waitKey(0)
cv2.destroyAllWindows()