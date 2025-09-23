#trackbar thay doi tuong phan, anh sang
import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
# cv2.namedWindow('trackbar')
# def nothing(x):
#     pass
# cv2.createTrackbar("tuong phan","trackbar",10,30,nothing)
# cv2.createTrackbar("do sang","trackbar",-50,80,nothing)
# while True:
#     a = cv2.getTrackbarPos("tuong phan","trackbar")/10.0
#     b = cv2.getTrackbarPos("do sang", "trackbar")
#     chinh = cv2.convertScaleAbs(img, alpha = a, beta = b)
#     cv2.imshow("trackbar", chinh)
#     if cv2.waitKey(1) == 27:
#         break
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#doi mau anh
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# amban = 255-rgb

# plt.subplot(131)
# plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB))
# plt.title("anh mac dinh")
# plt.axis("off")

# plt.subplot(132)
# plt.imshow(gray,cmap = "gray")
# plt.title("anh xam")
# plt.axis("off")

# plt.subplot(133)
# plt.imshow(amban)
# plt.title("anh xam")
# plt.axis("off")

#Dịch ảnh với khoảng cách nhập vào từ bàn phím
# h, w = img.shape[:2]
# tx = int(input("Nhập khoảng dịch theo trục X: "))
# ty = int(input("Nhập khoảng dịch theo trục Y: "))

# M = np.float32([[1,0,tx],[0,1,ty]])
# result = cv2.warpAffine(img, M, (w,h))
# cv2.imshow("dich chuyen anh", result)

# Dịch ảnh bằng trackbar
# h, w = img.shape[:2]
# cv2.namedWindow("Trackbar")

# def move(_=None):
    
#     tx = cv2.getTrackbarPos("X", "Trackbar") - w//2
#     ty = cv2.getTrackbarPos("Y", "Trackbar") - h//2
    
#     M  = np.float32([[1, 0, tx], [0, 1, ty]])
#     result =  cv2.warpAffine(img, M, (w, h))
#     cv2.imshow("Trackbar",result)

# cv2.createTrackbar("X", "Trackbar", w//2, w, move)
# cv2.createTrackbar("Y", "Trackbar", h//2, h, move)

# Thay đổi kích thước ảnh
# h, w = img.shape[:2]
# print(f"Anh co kich thuoc la: width={w}, height={h}")

# new_w = int(input("Nhập chiều rộng mới: "))
# new_h = int(input("Nhập chiều cao mới: "))

# resized = cv2.resize(img, (new_w, new_h))
# cv2.imshow("Anh Goc", img)
# cv2.imshow(f"Anh {new_w}x{new_h}", resized)


# h, w = img.shape[:2]
# print (f"Kich thuoc anh la: w={w}, h={h}")
# new_w = int(input("nhap w moi:"))
# new_h = int(input("nhap h moi"))
# resized = cv2.resize(img, (new_w,new_h))
# cv2.imshow("resize",resized)

# Xoay ảnh với góc xoay nhập vào từ bàn phím
# h, w = img.shape[:2]
# angle = float(input("Nhập góc xoay (độ, + ngược kim đồng hồ): "))
# M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
# rotated = cv2.warpAffine(img, M, (w, h))
# cv2.imshow("Xoay anh", rotated)

#Xoay ảnh bằng trackbar
h, w = img.shape[:2]
cv2.namedWindow("Rotate")

def rotate(_=None):
    do = cv2.getTrackbarPos("do", "Rotate") - 180  
    M   = cv2.getRotationMatrix2D((w/2, h/2), do, 1)
    cv2.imshow("Rotate", cv2.warpAffine(img, M, (w, h)))

cv2.createTrackbar("do", "Rotate", 180, 360, rotate)
rotate()

cv2.waitKey(0)
cv2.destroyAllWindows()


