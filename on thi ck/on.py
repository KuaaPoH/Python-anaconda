import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\KENN\Desktop\tgmt1.png")
# h,w = img.shape[:2]
# print(f"chieu rong w = {w}, chieu cao h = {h}")
# x = int(input("nhap toa do x: "))
# y = int(input("nhap toa do y: "))
# b, g, r = img[y,x]
# print(f"gia tri nao tai diem ({x},{y}) la B = {b}, G = {g}, R = {r}")
# a = float(input("nhap do tuong phan: "))
# chinh = cv2.convertScaleAbs(img, alpha=a, beta = 0)
# cv2.imshow("anh goc", img)
# cv2.imshow("anh chinh", chinh)
# cv2.imwrite(r"C:\Users\KENN\Desktop\anhchinh.png", chinh)

# def nothing(x):
#     pass
# cv2.namedWindow("trackbar")
# cv2.createTrackbar("kichco","trackbar", 1, 20, nothing)
# while True:
#     k = cv2.getTrackbarPos("kichco", "trackbar")
#     ksize = k * 2 + 1
#     if ksize == 0:
#         ksize += 1
#     trungbinh = cv2.blur(img, (ksize,ksize))
#     gau = cv2.GaussianBlur(img, (ksize,(ksize),0))
#     trungvi = cv2.medianBlur(img, ksize)
#     songphuong = cv2.bilateralFilter(img, ksize , 100 ,100)
#     cv2.imshow("trackbar", trungbinh)
#     if cv2.waitKey(1) == 27:
#         break

# gau = cv2.GaussianBlur(img, (5,5),0)
# gray = cv2.cvtColor(gau,cv2.COLOR_BGR2GRAY)
# thichnghi = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
# _, toiuu = cv2.threshold(gray,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# _, nhiphan = cv2.threshold(gray,0,255, cv2.THRESH_BINARY)
# candy = cv2.Canny(thichnghi, 100,200)
# lap = cv2.Laplacian(thichnghi, cv2.CV_64F)
# x = cv2.Sobel(thichnghi, cv2.CV_64F, 1,0,3)
# y = cv2.Sobel(thichnghi, cv2.CV_64F,0,1,3)
# hx = cv2.convertScaleAbs(x)
# hy=cv2.convertScaleAbs(y)
# sobel = cv2.addWeighted(hx,0.5,hy,0.5,0)

# plt.subplot(2,2,1)
# plt.title("anh goc")
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.axis("off")
# plt.subplot(2,2,2)
# plt.title("anh gau")
# plt.imshow(cv2.cvtColor(gau,cv2.COLOR_BGR2RGB))
# plt.axis("off")
# plt.subplot(2,2,3)
# plt.title("anh thich nghi")
# plt.imshow(thichnghi,cmap="gray")
# plt.axis("off")
# plt.subplot(2,2,4)
# plt.title("anh sobel")
# plt.imshow(sobel,cmap="gray")
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

# video.release()
video = cv2.VideoCapture(r"C:\Users\KENN\Desktop\theshorekeeper.mp4")
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video", frame)
    cv2.imshow("xam",gray)
    if cv2.waitKey(10) == ord("s"):
        cv2.imwrite(r"C:\Users\KENN\Desktop\theshorekeeperrr.png", gray)
    if cv2.waitKey(10) == ord("q"):
        break
fps = video.get(5)
anh = cv2.imread(r"C:\Users\KENN\Desktop\theshorekeeperrr.png")
kernal = np.ones((5,5), np.uint8)
gian = cv2.dilate(anh, kernal, iterations=1)
print(f"so khung hinh tren giay: {fps}")
cv2.imshow("anh", gian) 
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()