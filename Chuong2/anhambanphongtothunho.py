import cv2

img = cv2.imread("D:/CodeTGMT/Picture/xquang.jpg")
result = 255 - img
cv2.imshow("anh ban dau", img)
cv2.imshow("anh am ban", result)

img_to_cha_ba = cv2.resize(img, None,fx=2, fy=2,interpolation=cv2.INTER_LINEAR)
#cv2.INTER_AREA thu nho
#cv2.INTER_CUBIC cham nhung hieu qua hon

h, w=img.shape[:2]
cv2.imshow("anh to cha ba", img_to_cha_ba)

img_res = cv2.resize(img, (400,300))
cv2.imshow("anh thay doi", img_res)
#cat anh
cat_anh = img[80:200, 150:300]
cv2.imshow("cat anh", cat_anh)
#lay tu dau cho den 2
crop1 = img[:2,:2]


print (h,w)

cv2.waitKey(0)
cv2.destroyAllWindows()

