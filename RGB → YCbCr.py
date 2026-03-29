import cv2
import numpy as np

image = cv2.imread("gambar.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_norm = image_rgb / 255.0

R = img_norm[:, :, 0]
G = img_norm[:, :, 1]
B = img_norm[:, :, 2]

Y  = 0.299 * R + 0.587 * G + 0.114 * B
Cb = -0.168736 * R - 0.331264 * G + 0.5 * B
Cr = 0.5 * R - 0.418688 * G - 0.081312 * B

YCbCr = np.dstack((Y, Cb, Cr))
Cb_norm = (Cb - Cb.min()) / (Cb.max() - Cb.min() + 1e-6)
Cr_norm = (Cr - Cr.min()) / (Cr.max() - Cr.min() + 1e-6)
Y_img  = (Y * 255).astype(np.uint8)
Cb_img = (Cb_norm * 255).astype(np.uint8)
Cr_img = (Cr_norm * 255).astype(np.uint8)
YCbCr_img = (YCbCr[:, :, :3] * 255).astype(np.uint8)

cv2.imshow("Original", image)
cv2.imshow("Y (Luminance)", Y_img)
cv2.imshow("Cb", Cb_img)
cv2.imshow("Cr", Cr_img)
cv2.imshow("YCbCr (visual)", cv2.cvtColor(YCbCr_img, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()