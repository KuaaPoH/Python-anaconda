# 1. đọc ảnh, 2. hiện ảnh, 3. lưu ảnh, 4. đọc video, 5. đổi ảnh xám, 6. đổi ảnh màu, 7. hiện ảnh matplotlib, 8. cắt ảnh, 9. âm bản, 10. thay đổi kích thước ảnh
# 11. độ sáng, độ tương phản, 12. xoay ảnh, 13. dịch ảnh, 14. phối cảnh, 15. lọc trung bình, 16. lọc trung vị, 17. lọc gaussian, 18. lọc song phương
# 19. tách biên sobel, 20. tách biên canny, 21. tách biên laplacian, 22. phân ngưỡng nhị phân, 23.phân ngưỡng thích nghi, 24. phân ngưỡng tối ưu, 
# 25. biến đổi hình thái: co , giãn, mở, đóng , 26. tìm và vẽ contour, 27. tracbar


# 1. đọc ảnh, 2. hiện ảnh, 3. lưu ảnh
# import cv2

# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# cv2.imshow('hien anh',anh)
# cv2.imwrite('E:\doanhaha.jpg',anh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 4. đọc video

# import cv2

# video = cv2.VideoCapture(r"C:\Users\ACER\Pictures\1113.mp4")

# while True:
#     ret, frame = video.read()
#     cv2.imshow('hhh', frame)

#     if cv2.waitKey(1) == 27:
#         break
# cv2.destroyAllWindows()

# 5. đổi ảnh xám, 6. đổi ảnh màu, 7. hiện ảnh matplotlib

# import cv2
# import matplotlib.pyplot as plt

# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# anhxam = cv2.cvtColor(anh, cv2.COLOR_BGR2GRAY)
# anhmau = cv2.cvtColor(anh, cv2.COLOR_BGR2RGB)

# plt.subplot(1,3,1)
# plt.title('anh goc')
# plt.imshow(anh)
# plt.axis('off')

# plt.subplot(1,3,2)
# plt.title('anh xam')
# plt.imshow(anhxam, cmap = 'gray')
# plt.axis('off')

# plt.subplot(1,3,3)
# plt.imshow(anhmau,  cmap = 'gray')
# plt.axis('off')

# plt.show()

# 8. cắt ảnh

# import cv2
# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# h, w = anh.shape[:2]
# anhcat = anh[0:h//2, 0:w//2]
# cv2.imshow('anh cat', anhcat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 9. am ban

# import cv2
# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")

# anhamban = 255 - anh

# cv2.imshow('anh',anh)
# cv2.imshow('anhamban', anhamban)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 10. thay doi kich thuoc anh

# import cv2
# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg") 

# hh = cv2.resize(anh,(300,300))
# cv2.imshow('anh',anh)
# cv2.imshow('anhdoi',hh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 11. độ sáng, độ tương phản

# import cv2

# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg") 

# anhbdd = cv2.convertScaleAbs(anh, alpha = 1.5, beta = 50)

# cv2.imshow('dd',anhbdd)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 12. xoay ảnh
# import cv2
# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg") 
# h,w = anh.shape[:2]
# tam = cv2.getRotationMatrix2D((w//2,h//2), 45, 2)
# xoayanh = cv2.warpAffine(anh,tam,(w,h))
# cv2.imshow('anh xoay', xoayanh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 13. dịch ảnh

# import cv2
# import numpy as np

# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# h, w = anh.shape[:2]
# matran = np.float32([[1,0,100],[0,1,150]])
# ad = cv2.warpAffine(anh, matran, (w,h))
# cv2.imshow('anh',anh)
# cv2.imshow('anh dich chuyen', ad)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 14. phoi canh

# import cv2
# import numpy as np

# anh = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# h, w = anh.shape[:2]
# diemgoc = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
# diemphoi = np.float32([[0, 0], [w//2, 0],[0, h//2],[w//2, h//2]])
# matran = cv2.getPerspectiveTransform(diemgoc, diemphoi)
# anhphoi = cv2.warpPerspective(anh, matran, (w,h))
# cv2.imshow('anh',anhphoi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 15. lọc trung bình, 16. lọc trung vị, 17. lọc gaussian, 18. lọc song phương

# import cv2
# import matplotlib.pyplot as plt

# goc = cv2.imread(r"C:\Users\ACER\Pictures\pic1.jpg")
# anh = cv2.cvtColor(goc, cv2.COLOR_BGR2RGB)
# k = 9
# trungbinh = cv2.blur(anh,(k,k)) 
# trungvi = cv2.medianBlur(anh,k)
# gaussian = cv2.GaussianBlur(anh, (k,k),0)
# songphuong = cv2.bilateralFilter(anh, k,100,100)

# plt.subplot(1,4,1)
# plt.title('tb')
# plt.imshow(trungbinh)
# plt.axis('off')

# plt.subplot(1,4,2)
# plt.title('tv')
# plt.imshow(trungvi)
# plt.axis('off')

# plt.subplot(1,4,3)
# plt.title('gauu')
# plt.imshow(gaussian)
# plt.axis('off')

# plt.subplot(1,4,4)
# plt.title('sp')
# plt.imshow(songphuong)
# plt.axis('off')

# plt.show()

# 19. tách biên sobel, 20. tách biên canny, 21. tách biên laplacian

# import cv2
# import matplotlib.pyplot as plt

# goc = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# anh = cv2.cvtColor(goc, cv2.COLOR_BGR2GRAY)
# gauu = cv2.GaussianBlur(anh, (5,5),0)

# x = cv2.Sobel(gauu,cv2.CV_64F, 1, 0, ksize=3)
# y = cv2.Sobel(gauu, cv2.CV_64F, 0 , 1, ksize=3)
# hx = cv2.convertScaleAbs(x)
# hy = cv2.convertScaleAbs(y)
# sobel = cv2.addWeighted(hx , 0.5 , hy, 0.5, 0)

# canny = cv2.Canny(gauu,100,200)

# laplacian = cv2.Laplacian(gauu, cv2.CV_64F)

# plt.subplot(1,4,1)
# plt.title('anh xam')
# plt.imshow(anh, cmap = 'gray')
# plt.axis('off')

# plt.subplot(1,4,2)
# plt.title('anh sobel')
# plt.imshow(sobel, cmap = 'gray')
# plt.axis('off')


# plt.subplot(1,4,3)
# plt.title('anh canny')
# plt.imshow(canny, cmap = 'gray')
# plt.axis('off')


# plt.subplot(1,4,4)
# plt.title('anh lapla')
# plt.imshow(laplacian, cmap = 'gray')
# plt.axis('off')

# plt.show()

# 22. phân ngưỡng nhị phân, 23.phân ngưỡng thích nghi, 24. phân ngưỡng tối ưu


# import cv2
# import matplotlib.pyplot as plt

# goc = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# anh = cv2.cvtColor(goc, cv2.COLOR_BGR2GRAY)

# _,np = cv2.threshold(anh,127,255,cv2.THRESH_BINARY)

# thichnghi = cv2.adaptiveThreshold(anh,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# _, toiuu = cv2.threshold(anh, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# plt.subplot(1,4,1)
# plt.title('anh xam')
# plt.imshow(anh , cmap= 'gray')
# plt.axis('off')

# plt.subplot(1,4,2)
# plt.title('pnnp')
# plt.imshow(np, cmap= 'gray')
# plt.axis('off')

# plt.subplot(1,4,3)
# plt.title('pntn')
# plt.imshow(thichnghi, cmap= 'gray')
# plt.axis('off')

# plt.subplot(1,4,4)
# plt.title('pntu')
# plt.imshow(toiuu, cmap= 'gray')
# plt.axis('off')

# plt.show()


# 25. biến đổi hình thái: co , giãn, mở, đóng

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# goc = cv2.imread(r"C:\Users\ACER\Pictures\hinh-nen-mang-hinh-khoa-cute-06.jpg")
# anhxam = cv2.cvtColor(goc, cv2.COLOR_BGR2GRAY)

# blur = cv2.blur(anhxam,(5,5))

# thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# matna = np.ones((5,5),np.uint8)

# co = cv2.erode(thresh, matna,iterations=1)
# gian = cv2.dilate(thresh,matna,iterations=1)
# mo = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,matna)
# dong = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,matna)

# plt.subplot(1,4,1)
# plt.title('co')
# plt.imshow(co , cmap= 'gray')
# plt.axis('off')

# plt.subplot(1,4,2)
# plt.title('gian')
# plt.imshow(gian, cmap= 'gray')
# plt.axis('off')

# plt.subplot(1,4,3)
# plt.title('mo')
# plt.imshow(mo, cmap= 'gray')
# plt.axis('off')

# plt.subplot(1,4,4)
# plt.title('dong')
# plt.imshow(dong, cmap= 'gray')
# plt.axis('off')

# plt.show()

# 26. tìm và vẽ contour
import cv2
import numpy as np

goc = cv2.imread(r"C:\Users\ACER\Pictures\hhh.jpg")

anhxam = cv2.cvtColor(goc, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(anhxam,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

contour, hehehe = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

anhve = goc.copy()
cv2.drawContours(anhve,contour,-1,(0,255,0),2)

cv2.imshow('anhve',anhve)
cv2.waitKey(0)
cv2.destroyAllWindows()

