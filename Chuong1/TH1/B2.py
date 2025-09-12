import cv2
img = cv2.imread("C:/Picture/tgmt.png")
h, w= img.shape[:2]
x=int(input('Nhap toa do x:'))
y=int(input('Nhap toa do y:'))
b, g, r= img [y, x]
print(f'Gia tri mau tai diem anh co toa do ({x}, {y}): B:{b}, G: {g}, R: {r}')
cv2.imshow('Anh Goc', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

