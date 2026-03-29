import cv2
import numpy as np

image = cv2.imread("gambar.jpg")


kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharpened = cv2.filter2D(image, -1, kernel)

cv2.imshow("Original", image)
cv2.imshow("Sharpened (Laplacian)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()