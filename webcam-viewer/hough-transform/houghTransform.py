import cv2

cv2.namedWindow("Hough Transform (Ellipctic Recognition)", cv2.WINDOW_AUTOSIZE)
webcamFeed = cv2.VideoCapture(2)

while True:

  rval, frame = webcamFeed.read()
#  if not rval:
#    break
  
  frame = cv2.resize(frame, (852, 480))
  rval, frame = webcamFeed.read()
  
#  if cv2.waitKey(17) == 27 or cv2.getWindowProperty("Hough Transform (Ellipctic Regonition)", cv2.WND_PROP_VISIBLE) < 1:
#    break
  
  cv2.setWindowTitle("Hough Transform (Ellipctic Recognition)", "Hough Transform (Ellipctic Recognition)")
  
webcamFeed.release()
cv2.destroyAllWindows()
exit()