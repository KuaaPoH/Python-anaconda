# Khái niệm
# Bộ lọc Gauss (Gaussian Blur)là phép làm mờ ảnh sử dụng hàm phân bố chuẩn (Gaussian distribution) để tính trọng số cho các điểm ảnh lân cận.
# Khác với bộ lọc trung bình (mỗi điểm ảnh trong kernel đều có trọng số như nhau), Gaussian cho trọng số lớn hơn cho các pixel gần tâm, nhỏ dần khi xa tâm → làm mượt tự nhiên, ít mất chi tiết hơn.

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")

# Làm mờ Gaussian 5x5, sigmaX=1
gauss = cv2.GaussianBlur(img, (5,5), sigmaX=1)
# sigma càng béo thì ảnh càng mò

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Ảnh gốc"); plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(gauss, cv2.COLOR_BGR2RGB))
plt.title("Gaussian Blur 5x5, σ=1"); plt.axis("off")

plt.show()