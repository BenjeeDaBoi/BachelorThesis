import cv2
import numpy as np


# Blob Detection Parameters
params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100

params.filterByInertia = True
params.minInertiaRatio = 0

params.filterByConvexity = True
params.minConvexity = 0.7

params.filterByCircularity = True
params.minCircularity = 0.7

# Blob Detection doesn't work well on this type of image yet...
im = cv2.imread("./bw_erosion_histeq_threshold_220_255.png") # full_egg_bw_erosion_histeq_threshold_80_255.png
im = (255-im) # Invert for blob detection (only takes black pixels, not white pixels)

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blob Detection on HistEQ BW Threshold Image (220-255)", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()