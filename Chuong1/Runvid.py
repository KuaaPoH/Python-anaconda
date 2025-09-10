import cv2
cap = cv2.VideoCapture("C:/Video/theshorekeeper.mp4")
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video goc', frame)
    cv2.imshow('Mau xam',gray)
    if cv2.waitKey(10) == ord ('s'):
        cv2.imwrite('C:/Picture/Savepicture.png', frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()