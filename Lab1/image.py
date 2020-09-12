import numpy as np
import cv2 as cv
import time

print(np.__version__)
print(cv.__version__)

window_size = (640,  480)

cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.read()  # the first shot from my webcam is always a black rectangle, so I call it and then work with second shot
time.sleep(1)
ret, frame = cap.read()
if not ret:
    print("Can't receive frame")
    exit()

cv.imwrite('image.jpg', frame)
img = cv.imread('image.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

start_point_rect = (1, 23)
end_point_rect = (228, 432)
color_rect = (172, 19, 128)
thickness_rect = 10

start_point_line = (47, 387)
end_point_line = (300, 76)
color_line = (14, 88, 228)
thickness_line = 10

gray_rect = cv.rectangle(gray, start_point_rect, end_point_rect, color_rect, thickness_rect)
gray_rect_line = cv.line(gray_rect, start_point_line, end_point_line, color_line, thickness_line)

cv.imshow('frame', frame)
cv.imshow('gray', gray_rect_line)

cv.imwrite('gray_image.jpg', gray_rect_line)

cv.waitKey(0)

cap.release()
cv.destroyAllWindows()
