# Blob Detection
# zur Ermoeglichung der Bachelorarbeit

# Bloberkennung von Eiern mit
# Binary Thresholding zur Erkennung
# von Eiern im Nest

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

import cv2
import numpy as np

mode = 1

# Blob Detection Parameters
params = cv2.SimpleBlobDetector_Params()

# Area Parameter
params.filterByArea = True
params.minArea = 250

# Inertia Parameter
params.filterByInertia = True
params.minInertiaRatio = 0.2

# Convexity Parameter
params.filterByConvexity = True
params.minConvexity = 0.5

# Circularity Parameter
params.filterByCircularity = True
params.minCircularity = 0.6

# Load Image and Resize
image = cv2.imread("../0-test-images/brightsample01.tiff")
image = cv2.resize(image, (800, 450))

frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Binary Thresholding
if mode == 0:
    _, frame = cv2.threshold(frame, 140, 255, cv2.THRESH_BINARY_INV)
elif mode == 1:
  frame = cv2.GaussianBlur(frame, (3,3), 1)
  frame = cv2.Canny(frame, 60, 50)

# Instantiate Detector and detect blobs
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(frame)

# Draw Circles on detected Blobs
im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show Result
cv2.imshow("Blob Detection", im_with_keypoints)

# While Loop for exiting the program
while True:
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
exit()