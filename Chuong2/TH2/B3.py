import cv2

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
h, w = img.shape[:2]
print(f"Anh co kich thuoc la: width={w}, height={h}")

new_w = int(input("Nhập chiều rộng mới: "))
new_h = int(input("Nhập chiều cao mới: "))

resized = cv2.resize(img, (new_w, new_h))
cv2.imshow("Anh Goc", img)
cv2.imshow(f"Anh {new_w}x{new_h}", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()