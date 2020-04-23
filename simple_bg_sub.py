import cv2 as cv

# background subtraction
backSub = cv.createBackgroundSubtractorMOG2(history=200, varThreshold=20, detectShadows=False)

capture = cv.VideoCapture(0) # open first camera

# full screen
cv.namedWindow("Final", cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty("Final", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

# camera loop
while True:
    ret, frame = capture.read() # take in image
    if frame is None: # exit on blank frame
        break

    # update the background subtraction model
    fgMask = backSub.apply(frame)

    # use the mask created from the background subtractor to bitwise and the color and mask
    result = cv.bitwise_and(frame, frame, mask=fgMask)

    # show the final image
    cv.imshow('Final', result)

    # exit the program using q or ESC
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
