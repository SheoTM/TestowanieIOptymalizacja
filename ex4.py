import cv2
import numpy as np

blackscreen = np.zeros((300, 300, 3))
(centerX, centerY) = (blackscreen.shape[1] // 2,
                      blackscreen.shape[0] // 2)
red = (0, 0, 255)
cv2.rectangle(blackscreen, (centerX - 50, centerY - 50),
              (centerX + 50, centerY + 50), red, -1)
blue = (255, 0, 0)
cv2.circle(blackscreen, (centerX, centerY), 30, blue, -1)
cv2.imshow("Square and Circle", blackscreen)
cv2.waitKey(0)
cv2.destroyAllWindows()