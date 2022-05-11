import cv2


def detectContourEgg(frame):
  eggFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  eggFrame = cv2.blur(eggFrame, (10,10))
  
  im = cv2.adaptiveThreshold(eggFrame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
  contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  img = cv2.drawContours(frame, contours, -1, (0,255,75), 2)

  return img

cv2.namedWindow("Hough Transform (Elliptic Recognition)", cv2.WINDOW_AUTOSIZE)
webcamFeed = cv2.VideoCapture(1, cv2.CAP_DSHOW)

webcamFeed.set(cv2.CAP_PROP_FRAME_WIDTH, 852)
webcamFeed.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

  rval, frame = webcamFeed.read()
  if not rval:
    break

  frame = cv2.resize(frame, (852, 480))
  cv2.imshow("Hough Transform (Elliptic Recognition)", frame)
  
  cv2.imshow("Adaptive Thresholding", detectContourEgg(frame))
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  
webcamFeed.release()
cv2.destroyAllWindows()
exit()