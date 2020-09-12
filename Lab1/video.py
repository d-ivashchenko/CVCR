import numpy as np
import cv2 as cv
import os

path = os.getcwd()

print(np.__version__)
print(cv.__version__)

window_size = (640,  480)

cap = cv.VideoCapture(1)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('task1.avi', fourcc, 30, window_size, isColor=True)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break

    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('\x1b'):
        break

out.release()
cap.release()
cv.destroyAllWindows()

out_gray = cv.VideoWriter('task1_gray.avi', fourcc, 30, window_size, isColor=True)
cap_gray = cv.VideoCapture(path + '\\task1.avi')

start_point_rect = (1, 23)
end_point_rect = (228, 432)
color_rect = (172, 19, 128)
thickness_rect = 10

start_point_line = (47, 387)
end_point_line = (300, 76)
color_line = (14, 88, 228)
thickness_line = 10

while cap_gray.isOpened():
    ret, frame = cap_gray.read()
    if not ret:
        print("Can't receive frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    gray_rect = cv.rectangle(gray, start_point_rect, end_point_rect, color_rect, thickness_rect)
    gray_rect_line = cv.line(gray_rect, start_point_line, end_point_line, color_line, thickness_line)

    out_gray.write(gray_rect_line)
    cv.imshow('frame', gray_rect_line)
    if cv.waitKey(20) == ord('\x1b'):
        break

out_gray.release()
cap_gray.release()
cv.destroyAllWindows()
