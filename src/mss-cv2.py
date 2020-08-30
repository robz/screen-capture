# https://github.com/andrewzwicky/PUBGIS/blob/master/pubgis/minimap_iterators/live.py

import cv2
import numpy as np
import time
import mss

i = 0
start = time.thread_time()

sct = mss.mss()
size = 500
bounds = {'top': 0, 'left': 0, 'width': size, 'height': size}

while True:
    # make a screenshot
    img = sct.grab(bounds)
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # show the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

    i += 1
    delta = time.thread_time() - start
    print(i, delta, i / delta)


# make sure everything is closed when exited
cv2.destroyAllWindows()
