import cv2

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
cv2.imshow('xem anh',img)
#Ham thay doi do sang, do tuong phan
result = cv2.convertScaleAbs(img,alpha=2, beta=-100)


cv2.imshow('anh sau', result)
cv2.waitKey(0)
cv2.destroyAllWindows()