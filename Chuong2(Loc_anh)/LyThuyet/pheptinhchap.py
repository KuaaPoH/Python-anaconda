import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/CodeTGMT/Picture/tgmt.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
#kích thước kernel càng béo thì ảnh càng mờ
#3,3 /9

dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121)
plt.imshow(rgb)
plt.title('Original')
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title('Test')
plt.axis("off")

plt.show()