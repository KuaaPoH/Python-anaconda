import cv2

img = cv2.imread("D:/CodeTGMT/Picture/xquang.jpg")
result = 255 - img
cv2.imshow("anh ban dau", img)
cv2.imshow("anh am ban", result)

img_to_cha_ba = cv2.resize(img, None,fx=2, fy=2,interpolation=cv2.INTER_LINEAR)
#cv2.INTER_AREA thu nho
#cv2.INTER_CUBIC cham nhung hieu qua hon

img_res = cv2.resize(img, (400,300))
cv2.imshow("anh thay doi", img_res)


h, w=img.shape[:2]
cv2.imshow("anh to cha ba", img_to_cha_ba)


print (h,w)

cv2.waitKey(0)
cv2.destroyAllWindows()

