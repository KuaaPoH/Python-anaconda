import cv2
# Hàm callback được gọi mỗi khi kéo trackbar
def adjust(_=None):
    # Lấy giá trị từ 2 trackbar
    alpha = cv2.getTrackbarPos('Contrast', 'Adjust') / 100   # từ 0.0 → 3.0
    beta  = cv2.getTrackbarPos('Brightness', 'Adjust') - 100 # từ -100 → 100

    # Áp dụng thay đổi độ sáng và tương phản
    result = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    cv2.imshow('Adjust', result)
img = cv2.imread("D:/CodeTGMT/Picture/tgmt.png")
# Tạo cửa sổ để chứa trackbar
cv2.namedWindow('Adjust')

# Tạo 2 trackbar:
# Contrast: từ 0 → 300 (chia 100 để thành 0.0 → 3.0)
cv2.createTrackbar('Contrast',   'Adjust', 100, 300, adjust)
# Brightness: từ 0 → 200 (sau đó trừ 100 → -100 → +100)
cv2.createTrackbar('Brightness', 'Adjust', 100, 200, adjust)


# Hiển thị ảnh gốc ban đầu
adjust()

# Vòng lặp chờ phím 'q' để thoát
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()