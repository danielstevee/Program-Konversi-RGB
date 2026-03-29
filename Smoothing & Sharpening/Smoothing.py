import cv2
import numpy as np

image = cv2.imread("gambar.jpg")
smoothed = cv2.blur(image, (5, 5))

cv2.imshow("Original", image)
cv2.imshow("Smoothed (Mean Filter)", smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()