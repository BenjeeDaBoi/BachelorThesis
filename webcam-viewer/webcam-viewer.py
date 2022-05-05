import cv2 # pip install opencv-python
import os
from dotenv import load_dotenv # pip install python-dotenv

windowName = "Webcam View Eggs"

load_dotenv()
WEBCAM_RTSP_LINK = os.getenv('WEBCAM_RTSP_LINK')

cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
webcam = cv2.VideoCapture(WEBCAM_RTSP_LINK)

frame = None

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False

while rval:
    
    frame = cv2.resize(frame, (854, 480))
    
    cv2.imshow(windowName, frame)
    rval, frame = webcam.read()
    key = cv2.waitKey(17)
    
    if key == 27: # exit on ESC
        break
    
    if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
        break

# np.savetxt("./output.txt", frame.reshape((3,-1)), fmt="%s", header=str(frame.shape))

webcam.release()

if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) > 0:
    cv2.destroyWindow(windowName)