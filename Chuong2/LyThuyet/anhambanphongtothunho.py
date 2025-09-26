import cv2

img = cv2.imread("D:/CodeTGMT/Picture/xquang.jpg")
result = 255 - img  
cv2.imshow("anh ban dau", img)
cv2.imshow("anh am ban", result)
h,w = img.shape[:2]
print(h,w)
#img_to_cha_ba = cv2.resize(img, None,fx=2, fy=2,interpolation=cv2.INTER_LINEAR)

#cv2.INTER_LINEAR 
#cv2.INTER_AREA thu nhỏ
#cv2.INTER_CUBIC chậm nhưng hiểu quả


#cv2.imshow("anh to cha ba", img_to_cha_ba)

img_res = cv2.resize(img, (400,300))
cv2.imshow("anh thay doi", img_res)



cv2.waitKey(0)
cv2.destroyAllWindows()

