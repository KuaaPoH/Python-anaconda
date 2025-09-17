import cv2
import matplotlib.pyplot as plt
img = cv2.imread('D:/CodeTGMT/Picture/tgmt.png')
#cv2.imshow("anh", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("xam", gray)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


h, w = img.shape[:2]
print (h,w)
print (img[200,100])


plt.subplot(121)
plt.imshow(rgb)
plt.title("anh1")
plt.axis("off")

plt.subplot(122)
plt.imshow(gray, cmap="gray")
plt.title("anh2")
plt.axis("off")


chinh = cv2.convertScaleAbs(img, alpha=1, beta=100)
cv2.imshow("anh chinh", chinh)


#cap = cv2.VideoCapture("D:/CodeTGMT/Video/theshorekeeper.mp4")
#while True:
#    ret,frame = cap.read()
#    cv2.imshow("dz", frame)
#    if cv2.waitKey(10) == ord("q"):
#        break
#cap.release()
cv2.waitKey(0)

cv2.destroyAllWindows()