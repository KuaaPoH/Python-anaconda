import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\CodeTGMT\Picture\tgmt.png")
#cv2.imshow("anh", img)
#rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#plt.subplot(121)
#plt.imshow(rgb)
#plt.title("anh 1")
#plt.axis("off")
#plt.subplot(122)
#plt.imshow(gray, cmap="gray")
#plt.title("anh 2")
#plt.axis("off")

#h,w = img.shape[:2]
#print(h, w)

#cap=cv2.VideoCapture(r"D:\CodeTGMT\Video\theshorekeeper.mp4")
#while True:
#    ret,frame = cap.read()
#    cv2.imshow("video", frame)
#    if cv2.waitKey(10) == ord("q"):
#        break
#cap.release()

#chinh = cv2.convertScaleAbs(img,alpha=1,beta=100)
#cv2.imshow("mau chinh sua", chinh)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("mau xam", gray)

img = cv2.imread(r"D:\CodeTGMT\Picture\tgmt.png")
cv2.imshow("anh", img)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("mau xam", gray)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.imshow(rgb)
plt.title("anh 1")
plt.axis("off")
plt.subplot(122)
plt.imshow(gray, cmap = "gray")
plt.title("anh 2")
plt.axis("off")

chinh = cv2.convertScaleAbs(img, alpha = 1, beta = 100)
cv2.imshow("anh chinh", chinh)

h, w = img.shape[:2]
print(h,w)



cv2.waitKey(0)
cv2.destroyAllWindows()















