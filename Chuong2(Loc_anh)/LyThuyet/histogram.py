import cv2
import matplotlib.pyplot as plt

# Đọc ảnh màu và chuyển sang xám
img_color = cv2.imread("D:/CodeTGMT/Picture/cinematic.jpg")
gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# --- 1) Tính histogram ảnh gốc ---
# hist_size=256 mức xám, range [0,256)
hist = cv2.calcHist([gray], [0], None, [256], [0,256])

# --- 2) Cân bằng histogram ---
equalized = cv2.equalizeHist(gray)
hist_eq = cv2.calcHist([equalized], [0], None, [256], [0,256])

# --- 3) Hiển thị ---
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Ảnh xám gốc")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(equalized, cmap='gray')
plt.title("Ảnh sau cân bằng")
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist, color='black')
plt.title("Histogram gốc")
plt.xlim([0,256])

plt.subplot(2,2,4)
plt.plot(hist_eq, color='black')
plt.title("Histogram sau cân bằng")
plt.xlim([0,256])

plt.tight_layout()
plt.show()
