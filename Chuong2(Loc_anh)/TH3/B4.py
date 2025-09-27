import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/nhieu_muoi_tieu.jpg")

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

trungbinh = cv2.blur(img, (5, 5))
trungbinh = cv2.cvtColor(trungbinh, cv2.COLOR_BGR2RGB)

trungvi = cv2.medianBlur(img, 5)
trungvi = cv2.cvtColor(trungvi, cv2.COLOR_BGR2RGB)

gauss = cv2.GaussianBlur(img, (5, 5), 0)
gauss = cv2.cvtColor(gauss, cv2.COLOR_BGR2RGB)

songphuong = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
songphuong = cv2.cvtColor(songphuong, cv2.COLOR_BGR2RGB)

plt.subplot(231)
plt.imshow(rgb)
plt.title("Ảnh gốc")
plt.axis('off')

plt.subplot(232)
plt.imshow(trungbinh)
plt.title("Trung bình")
plt.axis('off')

plt.subplot(233)
plt.imshow(trungvi)
plt.title("Trung vị")
plt.axis('off')

plt.subplot(234)
plt.imshow(gauss)
plt.title("Gauss")
plt.axis('off')

plt.subplot(235)
plt.imshow(songphuong)
plt.title("Bilateral")
plt.axis('off')
plt.show()
