import cv2

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
h, w = img.shape[:2]

angle = float(input("Nhập góc xoay (độ, + ngược kim đồng hồ): "))

M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Xoay anh", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
