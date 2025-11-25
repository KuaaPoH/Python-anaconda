import cv2

img = cv2.imread(r"D:\CodeTGMT\Picture\pho.jpg")

bil = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

gray = cv2.cvtColor(bil, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Bilateral", bil)
cv2.imshow("Binary", binary)

cv2.imwrite(r"D:\CodeTGMT\Picture\anh3_binary.png", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
