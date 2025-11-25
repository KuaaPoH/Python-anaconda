import cv2

img = cv2.imread(r"D:\CodeTGMT\Picture\pho.jpg", cv2.IMREAD_GRAYSCALE)

win = "Trackbar Threshold"
cv2.namedWindow(win)

def change(_=None):
    t = cv2.getTrackbarPos("Thresh", win)
    _, th = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
    cv2.imshow(win, th)

cv2.createTrackbar("Thresh", win, 127, 255, change)
change()

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27: 
        break
    if k == ord('s'):
        t = cv2.getTrackbarPos("Thresh", win)
        _, th = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
        cv2.imwrite(r"D:\CodeTGMT\Picture\anh4_thresh.png", th)
        print("Đã lưu ảnh phân ngưỡng!")

cv2.destroyAllWindows()
