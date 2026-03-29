import cv2
import numpy as np

image = cv2.imread("gambar.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img_norm = image_rgb / 255.0

C = 1 - img_norm[:, :, 0]
M = 1 - img_norm[:, :, 1]
Y = 1 - img_norm[:, :, 2]

CMY = np.dstack((C, M, Y))

C_img = (C * 255).astype(np.uint8)
M_img = (M * 255).astype(np.uint8)
Y_img = (Y * 255).astype(np.uint8)
CMY_img = (CMY * 255).astype(np.uint8)

cv2.imshow("Original", image)
cv2.imshow("Cyan", C_img)
cv2.imshow("Magenta", M_img)
cv2.imshow("Yellow", Y_img)

cv2.imshow("CMY", cv2.cvtColor(CMY_img, cv2.COLOR_RGB2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()