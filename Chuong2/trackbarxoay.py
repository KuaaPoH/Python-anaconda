import cv2
import numpy as np

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
h, w = img.shape[:2]
cv2.namedWindow("Rotate")

def rotate(_=None):
    ang = cv2.getTrackbarPos("Angle", "Rotate") - 180   # dải -180 → +180
    M   = cv2.getRotationMatrix2D((w/2, h/2), ang, 1)
    cv2.imshow("Rotate", cv2.warpAffine(img, M, (w, h)))

cv2.createTrackbar("Angle", "Rotate", 180, 360, rotate)
rotate()

cv2.waitKey(0)
cv2.destroyAllWindows()
