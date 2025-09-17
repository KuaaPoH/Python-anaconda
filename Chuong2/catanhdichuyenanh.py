import cv2
import numpy as np
img = cv2.imread('D:/CodeTGMT/Picture/tgmt.png')

#dịch chuyển ảnh
h, w=img.shape[:2]
tx, ty = 50, -100 #sang phải, lên trên
M = np.float32([[1,0,tx],[0,1,ty]])
result = cv2.warpAffine(img, M, (w,h))
cv2.imshow("dich chuyen anh", result)

#cắt ảnh
cat_anh = img[80:200, 150:300]

#lấy từ đầu cho đến 2
crop1 = img[:2,:2]

top = img[:h//2,:]
botton = img[h//2:,:]
left = img[:,:w//2]
right = img[:,w//2:]


#cắt ảnh 1/4
left_corner = img[:h//2,:w//2] 


cv2.imshow("cat anh", top)
print (h,w)

cv2.waitKey(0)
cv2.destroyAllWindows()