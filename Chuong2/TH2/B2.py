import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
h, w = img.shape[:2]
left = img[:,:w//2]

gray = cv2.cvtColor(left,cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rgb_left =cv2.cvtColor(left,cv2.COLOR_BGR2RGB)
amban = 255 - rgb_left

plt.subplot(221)
plt.imshow(rgb)
plt.title("Anh Goc")
plt.axis("off")

plt.subplot(222)
plt.imshow(rgb_left)
plt.title("Anh Cat")
plt.axis("off")

plt.subplot(223)
plt.imshow(gray, cmap = "gray")
plt.title("Anh Xam")
plt.axis("off")

plt.subplot(224)
plt.imshow(amban)
plt.title("Anh Am Ban")
plt.axis("off")


cv2.waitKey(0)
cv2.destroyAllWindows()