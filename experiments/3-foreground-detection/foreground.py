# Vordergrund-Extraktion
# zur Ermoeglichung der Bachelorarbeit

# Vordergrund-Extraktion zur verbesserten
# Informations-Extraktion

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

import cv2
import numpy as np

# Function for foreground extraction
def changeImageByTrackbarValue(frame):
    
    frame = cv2.resize(frame, (800, 450))
    drawing = frame.copy()

    # Prepare Mask based on Image Shape
    mask = np.zeros(drawing.shape[:2], np.uint8)
    bgModel = np.zeros((1, 65), np.float64)
    fgModel = np.zeros((1, 65), np.float64)

    # Apply GrabCut Algorithm 
    rect = (287, 118, 217, 133)
    cv2.grabCut(drawing, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

    # Generate Real Foreground from Primary Foreground
    mask2 = np.where((mask==2) | (mask == 0), 0, 1).astype('uint8')
    drawing = drawing * mask2[:, :, np.newaxis]
                
    return drawing

# Read image and show on window
frame = cv2.imread('../0-test-images/brightsample01.tiff')
cv2.namedWindow('Foreground Extraction', cv2.WINDOW_AUTOSIZE)
cv2.imshow("Foreground Extraction", changeImageByTrackbarValue(frame))

while True:
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
exit()