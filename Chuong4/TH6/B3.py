import cv2
import numpy as np
from datetime import datetime
cap = cv2.VideoCapture('D:/CodeTGMT/Video/theshorekeeper.mp4') 

backsub = cv2.createBackgroundSubtractorMOG2(history=400, varThreshold=25, detectShadows=True)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

print("Nhấn 's' để lưu ảnh kết quả, 'q' để thoát.")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = backsub.apply(frame)  


    clean = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=1)
    clean = cv2.morphologyEx(clean,  cv2.MORPH_CLOSE, kernel, iterations=2)
    result = cv2.bitwise_and(frame, frame, mask=clean)

    cv2.imshow("Webcam", frame)
    cv2.imshow("Result (foreground only)", result)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break
    if k == ord('s'):
        fn = f"D:/CodeTGMT/Picture/fg_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(fn, result)
        print("✔ Đã lưu:", fn)

cap.release()
cv2.destroyAllWindows()
