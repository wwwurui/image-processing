# -*- coding:utf-8 -*-

import cv2
import numpy as np

# Step1. 加载图像
img = cv2.imread('C:\\Users\\WuRui\\Pictures\\Camera Roll\\zhijia.jpg')
print(type(img))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step2.阈值分割，将图像分为黑白两部分
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

# Step3. 对图像进行“开运算”，先腐蚀再膨胀
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
cv2.imshow("opening", opening)
cv2.waitKey(0)

# Step4. 对“开运算”的结果进行膨胀，得到大部分都是背景的区域
sure_bg = cv2.dilate(opening, kernel, iterations=3)
cv2.imshow("sure_bg", sure_bg)
cv2.waitKey(0)

# Step5.通过distanceTransform获取前景区域
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.6 * dist_transform.max(), 255, 0)
# cv2.imshow("sure_fg", sure_fg)

# Step6. sure_bg与sure_fg相减,得到既有前景又有背景的重合区域
sure_fg = np.uint8(sure_fg)
unknow = cv2.subtract(sure_bg, sure_fg)

# Step7. 连通区域处理
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknow==255] = 0

# Step8.分水岭算法
markers = cv2.watershed(img, markers)
img[markers == -1] = [0, 255, 0]

cv2.imshow("coins", img)
cv2.waitKey(0)
