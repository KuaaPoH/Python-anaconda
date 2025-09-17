import cv2
img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
cv2.namedWindow('dc')
def nothing(x):
    pass
cv2.createTrackbar("tuong phan","dc",10,30,nothing)
cv2.createTrackbar("do sang","dc",-50,80,nothing)
while True:
    a = cv2.getTrackbarPos("tuong phan","dc")/10.0
    b = cv2.getTrackbarPos("do sang", "dc")
    chinh = cv2.convertScaleAbs(img, alpha = a, beta = b)
    cv2.imshow("dc", chinh)
    if cv2.waitKey(1) == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
