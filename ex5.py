import cv2
import numpy as np

blackscreen = np.zeros((300, 300, 3))
(centerX, centerY) = (blackscreen.shape[1] // 2,
                      blackscreen.shape[0] // 2)
blue = (255, 0, 0)

for size in range(0, 150, 20):
    cv2.rectangle(blackscreen, (centerX - size, centerY - size),
                  (centerX + size, centerY + size), blue, 1)

cv2.imshow("Squares", blackscreen)
cv2.waitKey(0)
cv2.destroyAllWindows()