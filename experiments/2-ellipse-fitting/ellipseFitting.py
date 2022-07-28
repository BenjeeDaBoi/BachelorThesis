# Ellipse Fitting
# zur Ermoeglichung der Bachelorarbeit

# Ellipse Fitting von Elliptoiden Objekten
# mit Kantenerkennung

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

import cv2
import random as rng
import numpy as np
import math

# Generating seed for color generation
rng.seed(42069)

maxHysteresis = 255
hysteresis = 65

minMinorAxis = 5
maxMinorAxis = 20

minMajorAxis = 5
maxMajorAxis = 20

# Flag to prevent colouring ellipse every frame
hysteresisChanged = True

# Trackbar Value Change for Canny Hysteresis Value
def on_hysteresis_change(value):
    global hysteresis
    global hysteresisChanged
    
    hysteresis = value
    hysteresisChanged = True

# Function for value changes and ellipse fitting
def changeImageByTrackbarValue(frame):
    
    frame = cv2.resize(frame, (427, 240))
    
    global hysteresisChanged
    if hysteresisChanged == False:
        return None
    
    # Canny Detection
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameGray = cv2.GaussianBlur(frame, (9, 9), sigmaX=1, sigmaY=1)
    canny_output = cv2.Canny(frameGray, hysteresis, hysteresis)
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find ellipses for each contour
    minEllipse = [None]*len(contours)
    for i, c in enumerate(contours):
        if c.shape[0] > 5:
            minEllipse[i] = cv2.fitEllipse(c)

    # Remove all None entries
    minEllipse = list(filter(None, minEllipse))

    # Prevent writing over original image (needed for value changes)
    drawing = frame.copy()
    
    # Iterate through all ellipses under specific condition
    for elli in minEllipse:
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        ellipseMajor, ellipseMinor = elli[1]
        
        if ellipseMinor >= minMinorAxis and ellipseMajor <= maxMinorAxis:
            if ellipseMajor >= minMajorAxis and ellipseMajor <= maxMajorAxis:
                cv2.ellipse(drawing, elli, color, 1)  

    hysteresisChanged = False
    return drawing

# Read image and prepare the window
frame = cv2.imread('../0-test-images/brightsample03.tiff')
cv2.namedWindow("Ellipse Fitting", cv2.WINDOW_AUTOSIZE)

# Embed trackbar into window
cv2.createTrackbar('Canny Thresh:', "Ellipse Fitting", hysteresis, maxHysteresis, on_hysteresis_change)
changedFrame = None

# While Loop for Value Changes and exiting the program
while True:
    
    frame_copy = changeImageByTrackbarValue(frame)
    if frame_copy is not None:
        changedFrame = frame_copy
        
    cv2.imshow("Ellipse Fitting", changedFrame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('output.tiff', changedFrame)
        break
    
cv2.destroyAllWindows()
exit()