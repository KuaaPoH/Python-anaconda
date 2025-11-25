import cv2

img = cv2.imread('D:/CodeTGMT/Picture/tgmt.png')

resized = cv2.resize(img, width=300, height=200)

cv2.imshow('Resized', resized)