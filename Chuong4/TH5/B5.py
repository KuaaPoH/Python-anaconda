import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\CodeTGMT\Picture\pho.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th_bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

blur = cv2.GaussianBlur(gray, (5,5), 0)
_, th_otsu = cv2.threshold(blur, 0, 255,
                           cv2.THRESH_BINARY+cv2.THRESH_OTSU)

th_adp = cv2.adaptiveThreshold(gray, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY,
                               11, 2)

plt.figure(figsize=(10,6))
plt.subplot(2,2,1); plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.title("Ảnh gốc"); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(gray, cmap='gray'); plt.title("Ảnh xám"); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(th_bin, cmap='gray'); plt.title("Nhị phân 127"); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(th_otsu, cmap='gray'); plt.title("Otsu / Thích nghi"); plt.axis('off')
plt.tight_layout(); plt.show()
