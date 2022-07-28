# Canny Edge Detection
# zur Ermoeglichung der Bachelorarbeit

# Kantenerkennung von Eiern innerhalb
# des Eiernests

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

import cv2

blur_strength = 1
hysteresis_threshold = 1
threshold_value = 0

# Trackbar Value Change for Blur Value
def on_blur_change(value):
      
  if (value % 2 != 1):
    return
  
  global blur_strength
  blur_strength = value

# Trackbar Value Change for Binary Thresholding
def on_threshold_change(value):
  
  global threshold_value
  threshold_value = value
  
# Trackbar Value Change for Canny Hysteresis Value
def on_hysteresis_change(value):
  global hysteresis_threshold
  hysteresis_threshold = value

# Function for value changes
def changeImageByTrackbarValue(frame):
  
  frame = cv2.resize(frame, (427, 240))

  # Remove unnecessary patterns that could distort the detection
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame = cv2.GaussianBlur(frame, (blur_strength,blur_strength), 1)
  # _, frame = cv2.threshold(frame, threshold_value, 255, cv2.THRESH_BINARY)
  frame = cv2.Canny(frame, hysteresis_threshold, hysteresis_threshold)
  
  return frame
  
# Read Image and prepare the window
frame = cv2.imread("../0-test-images/brightsample01.tiff")
cv2.namedWindow("Edge Detection", cv2.WINDOW_AUTOSIZE)

# Embed trackbars into window
cv2.createTrackbar("Blur", "Edge Detection", 1, 50, on_blur_change)
cv2.createTrackbar("Hyst.", "Edge Detection", 1, 250, on_hysteresis_change)
cv2.createTrackbar("Thresh", "Edge Detection", 1, 255, on_threshold_change)

# While Loop for Value Changes and exiting the program
while True:

  frame_copy = changeImageByTrackbarValue(frame)
  cv2.imshow("Edge Detection", frame_copy)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  
cv2.destroyAllWindows()
exit()