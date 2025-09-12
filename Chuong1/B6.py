import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("C:/Picture/tgmt.png")   
img2 = cv2.imread("C:/Picture/tgmt1.png")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

rgb1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 6))

plt.subplot(2, 2, 1)
plt.imshow(rgb1)
plt.title("Ảnh 1 (Màu)")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gray1, cmap="gray")
plt.title("Ảnh 1 (Xám)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(rgb2)
plt.title("Ảnh 2 (Màu)")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(gray2, cmap="gray")
plt.title("Ảnh 2 (Xám)")
plt.axis("off")

plt.tight_layout()
plt.show()
