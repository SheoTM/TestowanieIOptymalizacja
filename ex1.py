import cv2
import numpy as np

blackscreen = np.zeros((300, 300, 3))
(centerX, centerY) = (blackscreen.shape[1] // 2,
                      blackscreen.shape[0] // 2)
blue = (255, 0, 0)
cv2.line(blackscreen, (centerX, centerY), (300, 300), blue, 2)
cv2.imshow("Blue line", blackscreen)
cv2.waitKey(0)
cv2.destroyAllWindows()