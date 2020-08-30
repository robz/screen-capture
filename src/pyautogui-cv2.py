# https://www.thepythoncode.com/article/make-screen-recorder-python

import cv2
import numpy as np
import pyautogui
import time

i = 0
start = time.thread_time()
print(start);

while True:
    # make a screenshot
    t0 = time.thread_time()
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    t1 = time.thread_time()
    print("t1 - t0 = ", t1 - t0);
    frame = np.array(img)
    # convert colors from BGR to RGB
    t2 = time.thread_time()
    print("t2 - t1 = ", t2 - t1);
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # show the frame
    t3 = time.thread_time()
    print("t3 - t2 = ", t3 - t2);
    cv2.imshow("screenshot", frame)
    t4 = time.thread_time()
    print("t4 - t3 = ", t4 - t3);
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

    i += 1
    delta = time.thread_time() - start
    print(i, delta, i / delta)


# make sure everything is closed when exited
cv2.destroyAllWindows()
