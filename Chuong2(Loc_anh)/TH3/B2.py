import cv2
import pytesseract
import matplotlib.pyplot as plt

img = cv2.imread('D:/CodeTGMT/Picture/text.png')
chinh = cv2.convertScaleAbs(img, alpha = -1, beta = 200)
gray = cv2.cvtColor(chinh, cv2.COLOR_BGR2GRAY)

config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang='vie', config=config)

print("Đọc text trong ảnh: ")
print(text)

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Ảnh gốc")
plt.axis('off')

plt.subplot(122)
plt.imshow(gray, cmap='gray')
plt.title("Ảnh xám đã chỉnh")
plt.axis('off')
plt.show()
