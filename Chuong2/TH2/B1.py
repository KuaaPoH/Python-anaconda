import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
amban = 255 - gray

plt.subplot(131)
plt.imshow(rgb)
plt.title("Anh Goc")
plt.axis("off")

plt.subplot(132)
plt.imshow(gray, cmap = "gray")
plt.title("Anh Xam")
plt.axis("off")

plt.subplot(133)
plt.imshow(amban)
plt.title("Anh Am Ban")
plt.axis("off")


cv2.waitKey(0)
cv2.destroyAllWindows()