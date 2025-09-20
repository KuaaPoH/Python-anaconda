import cv2
import numpy as np

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
h, w = img.shape[:2]
cv2.namedWindow("Trackbar")

def move(_=None):
    tx = cv2.getTrackbarPos("X", "Trackbar") - w//2
    ty = cv2.getTrackbarPos("Y", "Trackbar") - h//2
    
    M  = np.float32([[1, 0, tx], [0, 1, ty]])
    result =  cv2.warpAffine(img, M, (w, h))
    cv2.imshow("Trackbar",result)

cv2.createTrackbar("X", "Trackbar", w//2, w, move)
cv2.createTrackbar("Y", "Trackbar", h//2, h, move)

cv2.waitKey(0)
cv2.destroyAllWindows()
