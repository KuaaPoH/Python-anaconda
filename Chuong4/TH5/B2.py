import cv2

img = cv2.imread(r"D:\CodeTGMT\Picture\pho.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th = cv2.adaptiveThreshold(gray, 255,
                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv2.THRESH_BINARY,
                           11, 2)

contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
vis = img.copy()
cv2.drawContours(vis, contours, -1, (0,255,0), 2)

cv2.imshow("Adaptive thresh", th)
cv2.imshow("Contours", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()
