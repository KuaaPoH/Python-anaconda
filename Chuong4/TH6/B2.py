import cv2
import numpy as np
import matplotlib.pyplot as plt

IMG_PATH = r"D:\CodeTGMT\Picture\tgmt.png"
SAVE_PATH = r"D:\CodeTGMT\Picture\TEST.png"

img = cv2.imread(IMG_PATH)
if img is None:
    raise FileNotFoundError("Không đọc được ảnh!")

h, w = img.shape[:2]

rect = (int(w*0.15), int(h*0.15), int(w*0.7), int(h*0.7))

mask = np.zeros((h, w), np.uint8) 
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

fgMask = np.where((mask==cv2.GC_FGD) | (mask==cv2.GC_PR_FGD), 255, 0).astype('uint8')
bgMask = np.where((mask==cv2.GC_BGD) | (mask==cv2.GC_PR_BGD), 255, 0).astype('uint8')

kernel = np.ones((3,3), np.uint8)
fgMask_clean = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel, iterations=1)
result = cv2.bitwise_and(img, img, mask=fgMask_clean)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1); plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.title("Ảnh gốc"); plt.axis('off')
plt.subplot(1,3,2); plt.imshow(fgMask_clean, cmap='gray');           plt.title("FG mask (clean)"); plt.axis('off')
plt.subplot(1,3,3); plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB)); plt.title("Kết quả tách nền"); plt.axis('off')
plt.tight_layout(); plt.show()

cv2.imwrite(SAVE_PATH, result)

