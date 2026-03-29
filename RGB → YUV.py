import cv2
import numpy as np

image = cv2.imread("gambar.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img_norm = image_rgb / 255.0

R = img_norm[:, :, 0]
G = img_norm[:, :, 1]
B = img_norm[:, :, 2]

Y = 0.299 * R + 0.587 * G + 0.114 * B
U = -0.14713 * R - 0.28886 * G + 0.436 * B
V = 0.615 * R - 0.51499 * G - 0.10001 * B

YUV = np.dstack((Y, U, V))

U_norm = (U - U.min()) / (U.max() - U.min() + 1e-6)
V_norm = (V - V.min()) / (V.max() - V.min() + 1e-6)

Y_img = (Y * 255).astype(np.uint8)
U_img = (U_norm * 255).astype(np.uint8)
V_img = (V_norm * 255).astype(np.uint8)

YUV_img = (YUV[:, :, :3] * 255).astype(np.uint8)

cv2.imshow("Original", image)

cv2.imshow("Y (Luminance)", Y_img)
cv2.imshow("U", U_img)
cv2.imshow("V", V_img)

cv2.imshow("YUV (visual)", cv2.cvtColor(YUV_img, cv2.COLOR_RGB2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()