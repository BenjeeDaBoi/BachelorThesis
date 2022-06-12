import cv2

from skimage.transform import hough_ellipse

blur_strength = 1
hysteresis_threshold = 1

def on_blur_change(value):
      
  if (value % 2 != 1):
    return
  
  global blur_strength
  blur_strength = value
  
  
  
def on_hysteresis_change(value):
  global hysteresis_threshold
  hysteresis_threshold = value

def detectContourEgg(frame):
  
  # Remove unnecessary patterns that could disrupt the detection
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame = cv2.GaussianBlur(frame, (blur_strength,blur_strength), 0)
  
  # Edge Detection (https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html)
  frame = cv2.Canny(frame, hysteresis_threshold, hysteresis_threshold)
  #frame = cv2.dilate(frame, None, iterations = 1)
  #frame = cv2.erode(frame, None, iterations = 1)
  
  return frame
  

cv2.namedWindow("Raw Video Feed", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Edge Detection", cv2.WINDOW_AUTOSIZE)
	
cv2.createTrackbar("Blur Strength", "Edge Detection", 1, 50, on_blur_change)
cv2.createTrackbar("Hysteresis Threshold", "Edge Detection", 1, 250, on_hysteresis_change)

frame = cv2.imread("source.PNG")
height, width, channels = frame.shape

while True:

  cv2.imshow("Raw Video Feed", frame)
  cv2.imshow("Edge Detection", detectContourEgg(frame))
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  
cv2.destroyAllWindows()
exit()