import cv2
import numpy as np

image = cv2.imread("gambar.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img_norm = image_rgb / 255.0

R = img_norm[:, :, 0]
G = img_norm[:, :, 1]
B = img_norm[:, :, 2]

K = 1 - np.max(img_norm, axis=2)

C = (1 - R - K) / (1 - K + 1e-6)
M = (1 - G - K) / (1 - K + 1e-6)
Y = (1 - B - K) / (1 - K + 1e-6)

CMYK = np.dstack((C, M, Y, K))

C_img = (C * 255).astype(np.uint8)
M_img = (M * 255).astype(np.uint8)
Y_img = (Y * 255).astype(np.uint8)
K_img = (K * 255).astype(np.uint8)

CMYK_img = (CMYK[:, :, :3] * 255).astype(np.uint8)  # tampilkan C,M,Y saja sebagai image

cv2.imshow("Original", image)

cv2.imshow("Cyan", C_img)
cv2.imshow("Magenta", M_img)
cv2.imshow("Yellow", Y_img)
cv2.imshow("Black (K)", K_img)

cv2.imshow("CMYK (visual)", cv2.cvtColor(CMYK_img, cv2.COLOR_RGB2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()