import cv2 # pip install opencv-python

windowName = "Webcam View Eggs"

cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 0 can also be URL of video stream !

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False

while rval:
    
    cv2.imshow(windowName, frame)
    rval, frame = webcam.read()
    key = cv2.waitKey(20)
    
    if key == 27: # exit on ESC
        break
    
    if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
        break

webcam.release()

if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) > 0:
    cv2.destroyWindow(windowName)