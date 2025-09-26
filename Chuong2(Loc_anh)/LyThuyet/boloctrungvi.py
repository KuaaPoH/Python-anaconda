# Khái niệm
# Bộ lọc trung vị là kỹ thuật làm mượt ảnh bằng cách thay giá trị của mỗi điểm ảnh bằng giá trị trung vị (median) của các pixel trong vùng lân cận.
# Rất hiệu quả trong việc khử nhiễu muối tiêu (salt & pepper noise) vì giá trị nhiễu cao/thấp bất thường sẽ bị trung vị loại bỏ.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/nhieu_muoi_tieu.jpg")

# Lọc trung vị với cửa sổ 5x5
median = cv2.medianBlur(img, 5)

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Ảnh gốc nhiễu muối tiêu")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB))
plt.title("Median Blur (ksize=5)")
plt.axis("off")

plt.show()
