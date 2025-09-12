import cv2

img = cv2.imread("C:/Picture/tgmt.png")
cv2.imshow('Anh Goc', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh Xam', gray)


cv2.waitKey(0)
cv2.destroyAllWindows()

