import cv2

img = cv2.imread("C:/Picture/tgmt.png")
cv2.imshow('Anh Goc', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh Xam', gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Anh HSV', hsv)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Anh RGB', rgb)
cv2.imwrite('C:/Picture/a.png', img)
h, w= img.shape[:2]
print(h,w)
print(img[200,100])
print(gray[200,100])
print(hsv[200,100])
print(rgb[200,100])

cv2.waitKey(0)
cv2.destroyAllWindows()

