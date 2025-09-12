import cv2
img = cv2.imread("C:/Picture/tgmt.png")
cv2.imshow('Anh Goc', img)

cv2.waitKey(0)
cv2.destroyAllWindows()