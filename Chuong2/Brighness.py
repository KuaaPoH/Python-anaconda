import cv2
img = cv2.imread("C:/Picture/theshorekeeper.png")
cv2.imshow('xem anh',img)
#Ham thay doi do sang, do tuong phan
result = cv2.convertScaleAbs(img,alpha=1.8, beta=-20)
cv2.imshow('anh sau', result)
cv2.waitKey(0)
cv2.destroyAllWindows()