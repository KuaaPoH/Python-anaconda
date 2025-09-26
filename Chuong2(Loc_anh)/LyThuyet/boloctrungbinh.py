# Khái niệm
# Là phương pháp làm trơn ảnh (smoothing / averaging).
# Mỗi điểm ảnh mới bằng trung bình cộng giá trị các điểm trong vùng lân cận kích thước k×k quanh nó.
# Giảm nhiễu dạng hạt (noise) nhưng cũng làm mờ chi tiết và biên.

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/noise.jpg")
blur3 = cv2.blur(img, (3,3))      # kernel 3x3
blur5 = cv2.blur(img, (9,9))      # kernel 9x9

plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Gốc')
plt.axis('off')

plt.subplot(132)
plt.imshow(cv2.cvtColor(blur3, cv2.COLOR_BGR2RGB))
plt.title('Blur 3x3')
plt.axis('off')

plt.subplot(133)
plt.imshow(cv2.cvtColor(blur5, cv2.COLOR_BGR2RGB))
plt.title('Blur 9x9')
plt.axis('off')


plt.show()