# # TRACKBAR LỌC ẢNH VỚI CÁC BỘ LỌC VỚI KÍCH THƯỚC LẤY TỪ TRACKBAR

# import cv2
# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# cv2.namedWindow("Mean Filter")

# def nothing(x):
#     pass
# # Trackbar chọn kích thước kernel
# cv2.createTrackbar("K", "Mean Filter", 1, 20, nothing)

# while True:
#     k = cv2.getTrackbarPos("K", "Mean Filter")

#     # Kernel phải là số lẻ và >= 1
#     if k < 1:
#         k = 1
#     if k % 2 == 0:
#         k += 1

#     trungbinh = cv2.blur(img,(k,k)) 
#     # trungvi = cv2.medianBlur(img,k)
#     # gaussian = cv2.GaussianBlur(img, (k,k),0)
#     # songphuong = cv2.bilateralFilter(img, k,100,100)

#     cv2.imshow("Mean Filter", trungbinh)

#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # KỊCH CHUYỂN ẢNH VỚI KHOẢNG CÁCH ĐƯỢC CHỌN TỪ TRACKBAR
# import cv2
# import numpy as np

# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# cv2.namedWindow("dich anh")
# def nothing(x):
#     pass
# # Trackbar chọn khoảng cách dịch chuyển
# cv2.createTrackbar('dx', "dich anh", 0, 100, nothing)
# cv2.createTrackbar('dy', "dich anh", 0, 100, nothing)

# while True:
#     dx = cv2.getTrackbarPos('dx', "dich anh")
#     dy = cv2.getTrackbarPos('dy', "dich anh")

#     h, w = img.shape[:2]
#     matran = np.float32([[1,0,dx],[0,1,dy]])
#     ad = cv2.warpAffine(img, matran, (w,h))

#     cv2.imshow("dich anh", ad)

#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()


# # TRACKBAR ĐỘ SÁNG, ĐỘ TƯƠNG PHẢN
# import cv2
# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# cv2.namedWindow("Do sang - Tuong phan")
# def nothing(x):
#     pass
# # Trackbar chọn độ sáng và độ tương phản
# cv2.createTrackbar('tuong phan', "Do sang - Tuong phan", 10, 30, nothing)
# cv2.createTrackbar('do sang', "Do sang - Tuong phan", 0, 100, nothing)

# while True:
#     tp = cv2.getTrackbarPos('tuong phan', "Do sang - Tuong phan")/10
#     ds = cv2.getTrackbarPos('do sang', "Do sang - Tuong phan")
#     # Điều chỉnh độ sáng và độ tương phản
#     res = cv2.convertScaleAbs(img, alpha=tp, beta=ds)
#     cv2.imshow("Do sang - Tuong phan", res)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR XOAY ẢNH VỚI GÓC XOAY ĐƯỢC CHỌN TỪ TRACKBAR
# import cv2
# import numpy as np

# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# cv2.namedWindow("Xoay anh")
# def nothing(x): pass
# # Trackbar chọn góc xoay
# cv2.createTrackbar('goc', "Xoay anh", 0, 360, nothing)
# while True:
#     xoay = cv2.getTrackbarPos('goc', "Xoay anh")
#     h, w = img.shape[:2]
#     tam = cv2.getRotationMatrix2D((w//2,h//2), xoay, 1)
#     xoayanh = cv2.warpAffine(img,tam,(w,h))
#     cv2.imshow("Xoay anh", xoayanh)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR PHÂN NGƯỠNG ẢNH NHI PHAN
# import cv2
# img = cv2.imread(r"C:\Anh\Daidien.jpg",0)
# cv2.namedWindow("Phan nguong anh")
# def nothing(x): pass
# # Trackbar chọn ngưỡng
# cv2.createTrackbar('nguong', "Phan nguong anh", 0, 255, nothing)
# while True:
#     nguong = cv2.getTrackbarPos('nguong', "Phan nguong anh")
#     _, nhiphan = cv2.threshold(img, nguong, 255, cv2.THRESH_BINARY)
#     cv2.imshow("Phan nguong anh", nhiphan)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR PHÂN NGƯỠNG THÍCH NGHI
# import cv2
# img = cv2.imread(r"C:\Anh\Daidien.jpg",0)
# cv2.namedWindow("Phan nguong thich nghi")
# def nothing(x): pass
# # Trackbar chọn kích thước khối
# cv2.createTrackbar('k', "Phan nguong thich nghi", 1,    100, nothing)
# while True:
#     k = cv2.getTrackbarPos('k', "Phan nguong thich nghi")
#     # Kernel phải là số lẻ và >= 3
#     if k < 3:
#         k = 3
#     if k % 2 == 0:
#         k += 1
#     nhiphan = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, k, 5)
#     cv2.imshow("Phan nguong thich nghi", nhiphan)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR PHÂN NGƯỠNG TỐI ƯU Otsu
# import cv2
# img = cv2.imread(r"C:\Anh\Daidien.jpg",0) #nhớ chuyển qua ảnh xám để làm
# cv2.namedWindow("Phan nguong Otsu")
# def nothing(x): pass
# # Trackbar chọn ngưỡng ban đầu
# cv2.createTrackbar('nguong', "Phan nguong Otsu", 0, 1, nothing)
# while True:
#     nguong = cv2.getTrackbarPos('nguong', "Phan nguong Otsu")
#     if nguong == 0:
#         _, nhiphan = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#     else:
#         _, nhiphan = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     cv2.imshow("Phan nguong Otsu", nhiphan)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR TÁCH BIÊN SOBEL
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# gauss = cv2.GaussianBlur(img, (3,3), 0)
# gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow("tach bien sobel")
# def nothing(x): pass
# # Trackbar chọn kích thước kernel
# cv2.createTrackbar('k', "tach bien sobel", 1, 10, nothing)
# while True:
#     k = cv2.getTrackbarPos('k', "tach bien sobel")
#     # Kernel phải là số lẻ và >= 1
#     if k < 1:
#         k = 1
#     if k % 2 == 0:
#         k += 1
#     sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=k)
#     sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=k)
#     grad_x = cv2.convertScaleAbs(sobelx)
#     grad_y = cv2.convertScaleAbs(sobely)
#     grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
#     cv2.imshow("tach bien sobel", grad)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR TÁCH BIÊN CANNY
# import cv2
# import numpy as np
# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# gauss = cv2.GaussianBlur(img, (3,3), 0)
# gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow("tach bien canny")
# def nothing(x): pass
# # Trackbar chọn ngưỡng thấp và cao
# cv2.createTrackbar('thap', "tach bien canny", 0, 255, nothing)
# cv2.createTrackbar('cao', "tach bien canny", 0, 255, nothing)
# while True:
#     thap = cv2.getTrackbarPos('thap', "tach bien canny")
#     cao = cv2.getTrackbarPos('cao', "tach bien canny")
#     canny = cv2.Canny(gray, thap, cao)
#     cv2.imshow("tach bien canny", canny)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()

# # TRACKBAR TÁCH BIÊN LAPLACIAN
# import cv2
# import numpy as np
# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# gauss = cv2.GaussianBlur(img, (3,3), 0)
# gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow("tach bien laplacian")
# def nothing(x): pass
# # Trackbar chọn kích thước kernel
# cv2.createTrackbar('k', "tach bien laplacian", 1, 10, nothing)
# while True:
#     k = cv2.getTrackbarPos('k', "tach bien laplacian")
#     # Kernel phải là số lẻ và >= 1
#     if k < 1:
#         k = 1
#     if k % 2 == 0:
#         k += 1
#     laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=k)
#     laplacian = cv2.convertScaleAbs(laplacian)
#     cv2.imshow("tach bien laplacian", laplacian)
#     if cv2.waitKey(1) == 27:  # ESC để thoát
#         break
# cv2.destroyAllWindows()



# import cv2, numpy as np
# import matplotlib.pyplot as plt

# img = cv2.imread(r"C:\Anh\Daidien.jpg")
# anhgoc = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# gauss = cv2.GaussianBlur(img, (3,3), 0)
# anhxam = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# _, touu = cv2.threshold(anhxam, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# canny = cv2.Canny(gauss, 100, 200)

# plt.subplot(1,4,1), plt.imshow(anhgoc), plt.title("anh ban dau"), plt.axis('off')
# plt.subplot(1,4,2), plt.imshow(anhxam, cmap='gray'), plt.title("anh xam"), plt.axis('off')
# plt.subplot(1,4,3), plt.imshow(touu, cmap='gray'), plt.title("phan nguong otsu"), plt.axis('off')
# plt.show()


import cv2, numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Anh\Daidien.jpg")
anhgoc = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
trungbinh = cv2.blur(img,(5,5))
anhxam = cv2.cvtColor(trungbinh, cv2.COLOR_RGB2GRAY)

thichnghi = cv2.adaptiveThreshold(anhxam, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5 )
lap = cv2.Laplacian(anhxam, cv2.CV_64F)
lap = cv2.convertScaleAbs(lap)

plt.subplot(1,3,1), plt.imshow(anhgoc), plt.title("anh goc"), plt.axis('off')
plt.subplot(1,3,2), plt.imshow(thichnghi, cmap = 'gray'), plt.title("thich nghi"), plt.axis('off')
plt.subplot(1,3,3), plt.imshow(lap, cmap = 'gray'), plt.title("lap "), plt.axis('off')
plt.show()