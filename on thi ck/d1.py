import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")

##c1
# h,w = img.shape[:2]
# print(f"chieu cao h = {h}, chieu rong w = {w}")

# x=int(input('Nhap toa do x:'))
# y=int(input('Nhap toa do y:'))
# b, g, r= img [y, x]
# print(f"mau tai toa do {x}, {y} la B = {b}, G = {g}, R = {r}")

# f=float(input("nhap do tuong phan: "))
# chinh = cv2.convertScaleAbs(img, alpha=f, beta=1)
# cv2.imshow('Anh chinh', chinh)
# cv2.imshow('Anh goc', img)

##c2
#tạo trackbar để đọc kích thước từ mặt nạ lọc, lọc ảnh bằng bộ lọc trung bình với kích thức mặt nạ lấy từ trackbar

def nothing(x):
    pass
cv2.namedWindow('trackbar')
cv2.createTrackbar('Kich thuoc', 'trackbar', 1, 20, nothing)
while True:
    k = cv2.getTrackbarPos('Kich thuoc', 'trackbar')
    ksize = k * 2 + 1
    if ksize % 2 == 0:
        ksize += 1
    #trung binh
    trungbinh = cv2.blur(img, (ksize, ksize))
    # #gauss
    # gau = cv2.GaussianBlur(img, (ksize, ksize), 0)
    # #song phuong
    # songphuong = cv2.bilateralFilter(img, d=ksize, sigmaColor=75, sigmaSpace=75)
    # #trung vị
    # trungvi = cv2.medianBlur(img, ksize)

    cv2.imshow('trackbar', trungbinh)
    if cv2.waitKey(1) & 0xFF == 27:
        break


#khử nhiễu ảnh bằng bộ lọc gauss, thực hiện phân ngưỡng ảnh bằng thuật toán phân ngưỡng tối ưu, tách biên ảnh bằng phương pháp tách biên canny, hiện các ảnh bằng matplotlib

# gau = cv2.GaussianBlur(img, (5, 5), 0)
# #phân ngưỡng tối ưu
# gray = cv2.cvtColor(gau, cv2.COLOR_BGR2GRAY)
# _, toiuu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# #phân ngưỡng nhị phân
# _, nhiphan = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# #phân ngưỡng thích nghi
# thichnghi = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# #tách biên canny
# canny = cv2.Canny(toiuu, 100, 200)
# #tách biên laplacian
# laplacian = cv2.Laplacian(toiuu, cv2.CV_64F)
# #tách biên sobel
# x = cv2.Sobel(toiuu,cv2.CV_64F, 1, 0, ksize=3)
# y = cv2.Sobel(toiuu, cv2.CV_64F, 0 , 1, ksize=3)
# hx = cv2.convertScaleAbs(x)
# hy = cv2.convertScaleAbs(y)
# sobel = cv2.addWeighted(hx , 0.5 , hy, 0.5, 0)

# #hiện ảnh
# plt.subplot(2, 2, 1)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.title("Ảnh gốc")
# plt.axis("off")
# plt.subplot(2, 2, 2)
# plt.imshow(cv2.cvtColor(gau, cv2.COLOR_BGR2RGB))
# plt.title("Bộ lọc Gauss")
# plt.axis("off")
# plt.subplot(2, 2, 3)
# plt.imshow(toiuu, cmap='gray')
# plt.title("Phân ngưỡng tối ưu")
# plt.axis("off")
# plt.subplot(2, 2, 4)
# plt.imshow(canny, cmap='gray')
# plt.title("Tách biên Canny")
# plt.axis("off")
# plt.show()

#đọc video từ tệp, in ra số khung hình trong 1 giây của video, xem video với màu xám
# video = cv2.VideoCapture(r"C:\Users\KENN\Desktop\theshorekeeper.mp4")
# while True:
#     ret,frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Video goc', frame)
#     cv2.imshow('Mau xam',gray)
#     if cv2.waitKey(10) == ord ('s'):
#         cv2.imwrite(r"C:\Users\KENN\Desktop\Savepicture.png", frame)
#     if cv2.waitKey(10) == ord('q'):
#         break
# fps = video.get(5)
# print('sokhunghinh/s',fps)
# frame_count = video.get(7)
# print('tongsokhunghinh:',frame_count)
# #thực hiện phép giãn nợ (dialate) đối với ảnh cắt được
# kernel = np.ones((5,5), np.uint8)
# gian = cv2.dilate(gray, kernel, iterations=1)
# co = cv2.erode(gray, kernel, iterations=1)
# mo = cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)
# dong = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
# cv2.imshow('gian', gian)
cv2.waitKey(0)
# video.release()
cv2.destroyAllWindows()