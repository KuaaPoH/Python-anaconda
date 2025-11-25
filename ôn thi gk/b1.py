import cv2
import matplotlib.pyplot as plt
import numpy as np
# 1. đọc ảnh
# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# cv2.imshow("anh", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# vid = cv2.VideoCapture(r"c:\Users\KENN\Desktop\theshorekeeper.mp4")
# while True:
#     ret, frame = vid.read()
#     cv2.imshow("video", frame)
#     if cv2.waitKey(1) == 27:
#         break
# cv2.destroyAllWindows()

# img = cv2.imread(r"c:\Users\KENN\Desktop\tgmt1.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.subplot(1,3,1)
# plt.title("mau xam")
# plt.imshow(gray, cmap="gray")
# plt.axis("off")

# plt.subplot(1,3,2)
# plt.title("mac dinh")
# plt.imshow(img)
# plt.axis("off")

# plt.subplot(1,3,3)
# plt.title("mau")
# plt.imshow(color)
# plt.axis("off")
# plt.show()

# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# h, w = img.shape[:2]
# catanh = img[0:h//2, 0:w//2]
# cv2.imshow("anh goc", img)
# cv2.imshow("anh cat", catanh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# amban = 255-img
# cv2.imshow("anh am ban", amban)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# chinh = cv2.resize(img, (300,300))
# cv2.imshow("anh chinh", chinh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# chinh = cv2.convertScaleAbs(img, alpha=1, beta=10)

# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# h, w= img.shape[:2]
# tam = cv2.getRotationMatrix2D((w//2, h//2), 45,2)
# xoayanh= cv2.warpAffine(img, tam,(w,h))
# cv2.imshow("xoay anh", xoayanh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# h, w = img.shape[:2]
# tx = 120
# ty = 100
# matran = np.float32([[1,0,tx],[0,1,ty]])
# dichanh = cv2.warpAffine(img, matran, (w,h))
# cv2.imshow("chinh", dichanh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# anh phoi
