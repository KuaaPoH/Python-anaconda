import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"c:\Users\KENN\Desktop\tgmt1.png")
# h, w = img.shape[:2]
# print(f"chieu cao h = {h}, chieu rong w = {w}")
# b, g, r = img [100,200]
# print(f"tai toa do 100,200 gia tri mau la B={b}, G={g}, R={r}")
# #cắt một phần ảnh với các tọa độ nhập vào từ bàn phím, lưu ảnh vừa cắt
# x1 = int(input("nhap toa do x1: "))
# y1 = int(input("nhap toa do y1: "))
# x2 = int(input("nhap toa do x2: "))
# y2 = int(input("nhap toa do y2: "))
# cat = img[y1:y2, x1:x2]

# cv2.imshow("anh goc", img)
# cv2.imshow("anh cat", cat)
# cv2.imwrite(r"c:\Users\KENN\Desktop\anhcat.png", cat)

#tạo trackbar để chọn kích thước dx, dy, dịch chuyển ảnh với khoảng cách theo trục x và trụ y là dx,dy lấy từ trackbar
# def nothing(x):
#     pass
# cv2.namedWindow('trackbar')
# cv2.createTrackbar('dx', 'trackbar', 0, 100, nothing)
# cv2.createTrackbar('dy', 'trackbar', 0, 100, nothing)
# while True:
#     dx = cv2.getTrackbarPos('dx', 'trackbar')
#     dy = cv2.getTrackbarPos('dy', 'trackbar')
#     M = np.float32([[1, 0, dx], [0, 1, dy]])
#     dichuyen = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
#     cv2.imshow('trackbar', dichuyen)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

#tạo trackbar để chọn hệ số phóng đại ảnh, phóng đại ảnh với hệ số phong đại lấy từ trackbar chia 2
# def nothing(x):
#     pass
# cv2.namedWindow('trackbar')
# cv2.createTrackbar('He so phong dai', 'trackbar', 1, 10, nothing)
# while True:
#     he_so = cv2.getTrackbarPos('He so phong dai', 'trackbar')
#     if he_so == 0:
#         he_so = 1
#     x = he_so / 2
#     y = he_so / 2
#     phongdai = cv2.resize(img, None, fx=x, fy=y)
#     cv2.imshow('trackbar', phongdai)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

#tạo trackbar xoay ảnh với góc xoay lấy từ trackbar
# h, w = img.shape[:2]
# def nothing(x):
#     pass

# cv2.namedWindow('trackbar')
# cv2.createTrackbar('Goc xoay', 'trackbar', 0, 360, nothing)
# while True:
#     gocxoay = cv2.getTrackbarPos('Goc xoay', 'trackbar')
#     M = cv2.getRotationMatrix2D((w/2, h/2), gocxoay, 1)
#     xoay = cv2.warpAffine(img, M, (w, h))
#     cv2.imshow('trackbar', xoay)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break


#thực hiện phép mở ảnh, vẽ contour của ảnh
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#phép mở ảnh
kernel = np.ones((5, 5), np.uint8)
mo = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
#tìm contour
contours, _ = cv2.findContours(mo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
cv2.imshow("Anh goc", img)
cv2.imshow("Anh mo", mo)
cv2.imshow("Anh contour", img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()