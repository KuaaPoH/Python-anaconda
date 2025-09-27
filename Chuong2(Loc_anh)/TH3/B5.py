import cv2

img = cv2.imread("D:/CodeTGMT/Picture/nhieu_muoi_tieu.jpg")

cv2.namedWindow("trackbar")

def median(_=None):
    k = cv2.getTrackbarPos("ksize","trackbar")
    trungvi = cv2.medianBlur(img, k)
    cv2.imshow("trackbar", trungvi)

cv2.createTrackbar("ksize", "trackbar", 1, 15, median)

cv2.waitKey(0)
cv2.destroyAllWindows()
