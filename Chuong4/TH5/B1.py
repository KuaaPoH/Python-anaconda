import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\CodeTGMT\Picture\pho.jpg")

x1 = int(input("Nhập x trên trái: "))
y1 = int(input("Nhập y trên trái: "))
x2 = int(input("Nhập x dưới phải: "))
y2 = int(input("Nhập y dưới phải: "))

crop = img[y1:y2, x1:x2]

gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)
_, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
plt.title("Ảnh cắt")
plt.axis('off')

plt.subplot(1,3,2); plt.imshow(gray, cmap='gray'); plt.title("Ảnh xám"); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(otsu, cmap='gray'); plt.title("Otsu"); plt.axis('off')
plt.tight_layout(); plt.show()
