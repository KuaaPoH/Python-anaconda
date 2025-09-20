import cv2
import numpy as np
img = cv2.imread('D:/CodeTGMT/Picture/tgmt.png')

h, w = img.shape[:2]
tx = int(input("Nhập khoảng dịch theo trục X: "))
ty = int(input("Nhập khoảng dịch theo trục Y: "))

M = np.float32([[1,0,tx],[0,1,ty]])
result = cv2.warpAffine(img, M, (w,h))
cv2.imshow("dich chuyen anh", result)


cv2.waitKey(0)
cv2.destroyAllWindows()