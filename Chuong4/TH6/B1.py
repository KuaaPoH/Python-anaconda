import cv2
import numpy as np
import matplotlib.pyplot as plt

IMG_PATH = r"D:\CodeTGMT\Picture\vantay.png"

img = cv2.imread(IMG_PATH)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
denoise = cv2.medianBlur(gray, 3)             

_, otsu = cv2.threshold(denoise, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((3,3), np.uint8)
eroded  = cv2.erode(otsu,  kernel, iterations=1)
dilated = cv2.dilate(otsu, kernel, iterations=1)
opening = cv2.morphologyEx(otsu, cv2.MORPH_OPEN,  kernel, iterations=1)
closing = cv2.morphologyEx(otsu, cv2.MORPH_CLOSE, kernel, iterations=1)

plt.figure(figsize=(12,8))
plt.subplot(2,3,1); plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.title("Ảnh gốc"); plt.axis('off')
plt.subplot(2,3,2); plt.imshow(gray, cmap='gray');                    plt.title("Ảnh xám"); plt.axis('off')
plt.subplot(2,3,3); plt.imshow(denoise, cmap='gray');                 plt.title("Khử nhiễu"); plt.axis('off')
plt.subplot(2,3,4); plt.imshow(otsu, cmap='gray');                    plt.title("Otsu"); plt.axis('off')
plt.subplot(2,3,5); plt.imshow(opening, cmap='gray');                 plt.title("Opening"); plt.axis('off')
plt.subplot(2,3,6); plt.imshow(closing, cmap='gray');                 plt.title("Closing"); plt.axis('off')
plt.tight_layout(); plt.show()

