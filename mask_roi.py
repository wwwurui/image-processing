"""
     纯色背景ROI提取
"""


import cv2 as cv
import numpy as np

# 利用掩模（mask）技术提取纯色背景下roi区域
src = cv.imread('C:\\Users\\WuRui\\Pictures\\Camera Roll\\image.png')
cv.namedWindow('src', cv.WINDOW_NORMAL)
cv.imshow('src', src)
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)       # 转换成hsv色彩风格
mask = cv.inRange(hsv, (0, 0, 0), (180, 255, 46))        # 利用inRange产生纯色背景的mask min(h,s,v),max(h,s,v)
cv.namedWindow('mask1', cv.WINDOW_NORMAL)
cv.imshow('mask1', mask)
# 获取mask
mask = cv.bitwise_not(mask)
cv.namedWindow('mask2', cv.NORM_HAMMING)
cv.imshow('mask2', mask)
timg1 = cv.bitwise_and(src, src, mask=mask)
cv.namedWindow('timg', cv.NORM_HAMMING)
cv.imshow('timg1', timg1)
# 生成纯色背景
background = np.zeros(src.shape, src.dtype)
background[:, :, :] = 0
# 将目标贴到背景中
mask = cv.bitwise_not(mask)
dst = cv.bitwise_or(timg1, background, mask=mask)
cv.namedWindow('dst1', cv.NORM_HAMMING)
cv.imshow('dst1', dst)
dst = cv.add(dst, timg1)
cv.imshow('dst2', dst)

k = cv.waitKey(0) & 0xff     # 输入命令k，进行操作 esc=27,
if k == 27:
    cv.destroyAllWindows()     # 关闭显示窗口
elif k == ord('s'):
    cv.imwrite('savesrc.png', src)
    cv.destroyAllWindows()

