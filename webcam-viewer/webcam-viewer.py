from threading import Thread
from time import sleep
from dotenv import load_dotenv # pip install python-dotenv

import cv2 # pip install opencv-python
import os


class WebcamViewer:
    
    windowName = "Webcam View Eggs"
    webcamFeed = None
    WEBCAM_RTSP_LINK = None
    reconnectThread = None
    
    def __init__(self):
        
        load_dotenv()
        self.WEBCAM_RTSP_LINK = os.getenv('WEBCAM_RTSP_LINK')
        
        self.__connectToRTSPStream__()
        
        
    def __connectToRTSPStream__(self):
        
        if self.webcamFeed == None:
            cv2.namedWindow(self.windowName, cv2.WINDOW_AUTOSIZE)
            
        self.webcamFeed = cv2.VideoCapture(self.WEBCAM_RTSP_LINK, cv2.CAP_FFMPEG)
        self.__handleWebcamFeed__()
        
    def __handleWebcamFeed__(self):
        
        rval, frame = self.webcamFeed.read()
        closeProgram = False
        
        while rval:
            
            frame = cv2.resize(frame, (854, 480))
            
            cv2.imshow(self.windowName, frame)
            rval, frame = self.webcamFeed.read()
            
            if cv2.waitKey(17) == 27 or cv2.getWindowProperty(self.windowName, cv2.WND_PROP_VISIBLE) < 1:
                closeProgram = True
                break
        
        # If program was closed wrongly
        if closeProgram == False:
            print("[ERROR] RTSP Stream was closed wrongly, restarting RTSP Stream . . .")
            self.__connectToRTSPStream__()
        else:
            print("[DEBUG] Ending RTSP Stream . . .")
            self.webcamFeed.release()
            
            print("[DEBUG] Destroying all open windows . . .")
            cv2.destroyAllWindows()

            print("[DEBUG] Ending program . . .")
            exit()
        

test = WebcamViewer()