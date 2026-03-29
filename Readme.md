# 🔐 Color Image Processing & Conversion

Proyek ini merupakan implementasi **pengolahan citra berwarna (Color Image Processing)** menggunakan Python dan OpenCV.
Fokus utama dari proyek ini adalah melakukan **konversi model warna** serta **pengolahan citra** seperti smoothing dan sharpening.

---

## 🎯 Tujuan

* Memahami konsep berbagai **model warna**
* Mengimplementasikan konversi dari **RGB ke model warna lain**
* Menerapkan teknik **pengolahan citra berwarna**
* Menampilkan hasil visual dari setiap proses

---

## 🧠 Konsep Dasar

### 🎨 Model Warna

Model warna digunakan untuk merepresentasikan warna dalam bentuk numerik.
Setiap model memiliki fungsi dan kegunaan yang berbeda, seperti untuk display, printing, atau kompresi.

---

## 🔄 Konversi Model Warna

### 1. RGB → CMY

* Digunakan pada sistem printing dasar
* Rumus:

  * C = 1 - R
  * M = 1 - G
  * Y = 1 - B

Output:

* Original Image
* Cyan
* Magenta
* Yellow
* CMY (gabungan)

---

### 2. RGB → CMYK

* Pengembangan dari CMY dengan tambahan Black (K)
* Digunakan pada printer modern

Rumus:

* K = 1 - max(R, G, B)
* C = (1 - R - K) / (1 - K)
* M = (1 - G - K) / (1 - K)
* Y = (1 - B - K) / (1 - K)

Output:

* Original Image
* Cyan
* Magenta
* Yellow
* Black
* CMYK (visual)

---

### 3. RGB → HSI

* Berdasarkan persepsi manusia terhadap warna

Komponen:

* Hue → jenis warna
* Saturation → kejenuhan warna
* Intensity → tingkat kecerahan

Output:

* Original Image
* Hue
* Saturation
* Intensity
* HSI (visual)

---

### 4. RGB → YUV

* Digunakan pada sistem video

Komponen:

* Y → luminance (brightness)
* U & V → chrominance (warna)

Output:

* Original Image
* Y
* U
* V
* YUV (visual)

---

### 5. RGB → YCbCr

* Digunakan pada JPEG dan video digital

Komponen:

* Y → luminance
* Cb → blue difference
* Cr → red difference

Output:

* Original Image
* Y
* Cb
* Cr
* YCbCr (visual)

---

## 🛠️ Pengolahan Citra

### 1. Smoothing (Penghalusan)

* Digunakan untuk mengurangi noise pada citra
* Metode: Mean Filter (rata-rata tetangga piksel)

Output:

* Original Image
* Smoothed Image

---

### 2. Sharpening (Penajaman)

* Digunakan untuk memperjelas detail dan tepi citra
* Metode: Laplacian Filter

Output:

* Original Image
* Sharpened Image

---

## ⚙️ Teknologi yang Digunakan

* Python
* OpenCV
* NumPy

---

## ▶️ Cara Menjalankan

1. Install library:

```bash
pip install opencv-python numpy
```

2. Siapkan gambar:

```
gambar.jpg
```

3. Jalankan program sesuai kebutuhan:

```bash
python nama_file.py
```

---

## ⚠️ Catatan

* Semua perhitungan dilakukan dengan normalisasi (0–1)
* Beberapa komponen seperti U, V, Cb, Cr dinormalisasi ulang agar dapat ditampilkan
* Pengolahan citra dilakukan pada setiap channel RGB

---

## 📌 Kesimpulan

* Setiap model warna memiliki fungsi berbeda:

  * RGB → display
  * CMYK → printing
  * HSI → persepsi manusia
  * YUV / YCbCr → video & kompresi
* Teknik smoothing dan sharpening digunakan untuk meningkatkan kualitas citra

---

## 🚀 Pengembangan Selanjutnya

* Menggabungkan semua fitur dalam satu program
* Menambahkan GUI interaktif
* Menyimpan hasil konversi ke file

---

## ⚠️ Disclaimer

Proyek ini dibuat untuk tujuan **edukasi dan pembelajaran** dalam bidang pengolahan citra digital.  