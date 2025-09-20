import cv2

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
h, w = img.shape[:2]
img_to_cha_ba = cv2.resize(img, None,fx=1.5, fy=1.5,interpolation=cv2.INTER_LINEAR)


cv2.imshow("Anh Goc", img)
cv2.imshow("anh to cha ba", img_to_cha_ba)

cv2.waitKey(0)
cv2.destroyAllWindows()