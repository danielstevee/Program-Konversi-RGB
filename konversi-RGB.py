import cv2
import numpy as np

# =========================
# Load Image (BGR -> RGB)
# =========================
image = cv2.imread("gambar.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Normalize (0-1)
img_norm = image / 255.0


# =========================
# 1. RGB → CMY
# =========================
def rgb_to_cmy(img):
    cmy = 1 - img
    return cmy


# =========================
# 2. RGB → CMYK
# =========================
def rgb_to_cmyk(img):
    K = 1 - np.max(img, axis=2)
    
    C = (1 - img[:,:,0] - K) / (1 - K + 1e-6)
    M = (1 - img[:,:,1] - K) / (1 - K + 1e-6)
    Y = (1 - img[:,:,2] - K) / (1 - K + 1e-6)

    CMYK = np.dstack((C, M, Y, K))
    return CMYK


# =========================
# 3. RGB → HSI
# =========================
def rgb_to_hsi(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

    # Intensity
    I = (R + G + B) / 3

    # Saturation
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_rgb

    # Hue
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6
    theta = np.arccos(num / den)

    H = np.copy(theta)
    H[B > G] = 2 * np.pi - H[B > G]

    H = H / (2 * np.pi)

    HSI = np.dstack((H, S, I))
    return HSI


# =========================
# 4. RGB → YUV
# =========================
def rgb_to_yuv(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

    Y = 0.299*R + 0.587*G + 0.114*B
    U = -0.14713*R - 0.28886*G + 0.436*B
    V = 0.615*R - 0.51499*G - 0.10001*B

    YUV = np.dstack((Y, U, V))
    return YUV


# =========================
# 5. RGB → YCbCr
# =========================
def rgb_to_ycbcr(img):
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

    Y  = 0.299*R + 0.587*G + 0.114*B
    Cb = -0.168736*R - 0.331264*G + 0.5*B
    Cr = 0.5*R - 0.418688*G - 0.081312*B

    YCbCr = np.dstack((Y, Cb, Cr))
    return YCbCr


# =========================
# RUN SEMUA KONVERSI
# =========================
cmy   = rgb_to_cmy(img_norm)
cmyk  = rgb_to_cmyk(img_norm)
hsi   = rgb_to_hsi(img_norm)
yuv   = rgb_to_yuv(img_norm)
ycbcr = rgb_to_ycbcr(img_norm)


# =========================
# Tampilkan contoh hasil (RGB saja)
# =========================
cv2.imshow("RGB Image", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()