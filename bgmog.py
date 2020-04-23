import cv2 as cv
import numpy as np

backSub = cv.createBackgroundSubtractorMOG2()

capture = cv.VideoCapture(0)
cv.namedWindow("And", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("And", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

while True:
    kernel = np.ones((3, 3), np.uint8)
    ret, frame = capture.read()
    if frame is None:
        break

    fgMask = backSub.apply(frame)

    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    # cv.imshow('Frame', frame)
    # cv.imshow('FG Mask', fgMask)
    res = cv.bitwise_and(frame, frame, mask=fgMask)

    # gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

    # create a binary thresholded image
    _, binary = cv.threshold(fgMask, 225, 255, cv.THRESH_BINARY_INV)
    dilation = cv.dilate(binary, kernel, iterations=1)
    # cv.imshow('dilation', binary)
    # find the contours from the thresholded image
    image, contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # draw all contours
    res = cv.drawContours(res, contours, -1, (0, 255, 0), 1, lineType=cv.LINE_AA)

    cv.imshow('And', res)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
