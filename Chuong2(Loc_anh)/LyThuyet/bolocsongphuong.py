# Khái niệm
# Bộ lọc song phương (Bilateral Filter) là kỹ thuật làm mờ ảnh giảm nhiễu nhưng vẫn giữ biên (edge preserving).
# Nó kết hợp khoảng cách không gian và khoảng cách màu:
# Pixel gần về vị trí và giống màu với điểm trung tâm → trọng số cao.
# Pixel xa hoặc khác màu mạnh → trọng số thấp (không “trộn” qua biên).
# Kết quả: nền mịn nhưng đường biên vẫn rõ.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/noisevc.jpg")

# Bilateral Filter: d=9, sigmaColor=75, sigmaSpace=75
bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
bilateral1 = cv2.bilateralFilter(img, d=11, sigmaColor=200, sigmaSpace=200)

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Ảnh gốc"); plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))
plt.title("Bilateral Filter")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(bilateral1, cv2.COLOR_BGR2RGB))
plt.title("Bilateral Filter1")
plt.axis("off")

plt.show()
