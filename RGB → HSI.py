import cv2
import numpy as np

image = cv2.imread("gambar.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img_norm = image_rgb / 255.0

R = img_norm[:, :, 0]
G = img_norm[:, :, 1]
B = img_norm[:, :, 2]

I = (R + G + B) / 3

min_rgb = np.minimum(np.minimum(R, G), B)
S = 1 - (3 / (R + G + B + 1e-6)) * min_rgb

num = 0.5 * ((R - G) + (R - B))
den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6

theta = np.arccos(num / den)

H = np.copy(theta)
H[B > G] = 2 * np.pi - H[B > G]

H = H / (2 * np.pi)

HSI = np.dstack((H, S, I))

H_img = (H * 255).astype(np.uint8)
S_img = (S * 255).astype(np.uint8)
I_img = (I * 255).astype(np.uint8)

HSI_img = (HSI * 255).astype(np.uint8)

cv2.imshow("Original", image)

cv2.imshow("Hue", H_img)
cv2.imshow("Saturation", S_img)
cv2.imshow("Intensity", I_img)

cv2.imshow("HSI (visual)", cv2.cvtColor(HSI_img, cv2.COLOR_RGB2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()