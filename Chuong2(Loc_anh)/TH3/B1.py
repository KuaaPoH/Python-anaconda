import cv2
import numpy as np

img = cv2.imread("D:/CodeTGMT/Picture/white.jpg")

cv2.line(img, (50, 70), (300, 70), (0, 0, 255), 3, lineType=cv2.LINE_AA)

cv2.rectangle(img, (50, 100), (250, 220), color=(0, 255, 0), thickness=3)

cv2.circle(img, (150, 340), 60, (255, 0, 0),3)

cv2.ellipse(img, (450,70), (100,50), 0, 0, 360, (0,120,255), 3)

pts = np.array([(400, 200), (500, 300), (460, 420), (340, 420), (300,300)], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(50, 50, 200), thickness=3)

cv2.putText(img, "TranNgocHai", (50, 50),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.5,
            color=(0, 0, 0))


cv2.imshow("Ve", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

