import cv2
import numpy as np

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")

h0, w0 = img.shape[:2]        # kích thước gốc
cv2.namedWindow('Resize')

def nothing(x): pass

cv2.createTrackbar("Width",  "Resize", w0, w0*2, nothing)
cv2.createTrackbar("Height", "Resize", h0, h0*2, nothing)

while True:
  
    w = np.clip(cv2.getTrackbarPos("Width", "Resize"), 1, w0*2)
    h = np.clip(cv2.getTrackbarPos("Height", "Resize"), 1, h0*2)

    # Resize ảnh
    resized = cv2.resize(img, (int(w), int(h)), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Resize", resized)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
