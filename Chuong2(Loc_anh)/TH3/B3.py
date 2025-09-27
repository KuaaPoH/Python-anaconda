import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import textwrap

img = cv2.imread("D:/CodeTGMT/Picture/mau.jpg")
clone = img.copy()
clicks = []

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(clicks) < 4:
        clicks.append((x, y))
        cv2.circle(clone, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Chon 4 diem (ESC de xong)", clone)

cv2.imshow("Chon 4 diem (ESC de xong)", clone)
cv2.setMouseCallback("Chon 4 diem (ESC de xong)", click)
while True:
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()

anhchon = np.array(clicks, dtype=np.float32)

vis = img.copy()
cv2.polylines(vis, [anhchon.astype(np.int32).reshape(-1,1,2)], True, (0,0,255), 3, cv2.LINE_AA)

widthA  = np.linalg.norm(anhchon[1] - anhchon[0])  # TR - TL
widthB  = np.linalg.norm(anhchon[2] - anhchon[3])  # BR - BL
heightA = np.linalg.norm(anhchon[3] - anhchon[0])  # BL - TL
heightB = np.linalg.norm(anhchon[2] - anhchon[1])  # BR - TR
W = int(max(widthA, widthB))
H = int(max(heightA, heightB))

suabiendoi = np.float32([[0,0], [W-1,0], [W-1,H-1], [0,H-1]])
M = cv2.getPerspectiveTransform(anhchon, suabiendoi)
biendoi = cv2.warpPerspective(img, M, (W, H))

chinh = cv2.convertScaleAbs(biendoi, alpha=1.2, beta =20)

gray = cv2.cvtColor(biendoi, cv2.COLOR_BGR2GRAY)

config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(biendoi, lang='eng+vie', config=config)

plt.subplot(231)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Ảnh gốc")
plt.axis('off')

plt.subplot(232)
plt.imshow(cv2.cvtColor(vis,cv2.COLOR_BGR2RGB))
plt.title("Vùng chọn (4 góc)")
plt.axis('off')

plt.subplot(233)
plt.imshow(cv2.cvtColor(biendoi,cv2.COLOR_BGR2RGB))
plt.title("Sau biến đổi phối cảnh")
plt.axis('off')

plt.subplot(234)
plt.imshow(cv2.cvtColor(chinh,cv2.COLOR_BGR2RGB))
plt.title("Chỉnh sáng/tương phản)")
plt.axis('off')

plt.subplot(235)
plt.imshow(gray, cmap='gray')
plt.title("Ảnh xám")
plt.axis('off')

plt.subplot(236)
plt.axis('off')
plt.title("Đọc Text")
wrapped = "\n".join(textwrap.wrap(text.strip(), width=60))
plt.text(0.01, 0.98, wrapped, va='top', fontsize=10)

plt.show()
