from threading import Thread
from dotenv import load_dotenv
from datetime import datetime
from time import sleep

import cv2
import os


class WebcamViewer:

    ### Resolution: 720p ###
    WINDOW_WIDTH     = 1280
    WINDOW_HEIGHT    = 720
    
    ### Important Attributes ###
    windowName       = "PatEggAI v0.2 - by Benjamin Hartmann"
    webcamFeed       = None
    WEBCAM_RTSP_LINK = None
    
    def __init__(self):
        
        load_dotenv()
        self.WEBCAM_RTSP_LINK = os.getenv('WEBCAM_RTSP_LINK')
        
        self.__connectHandleWebcamFeed__()
        
    def __connectHandleWebcamFeed__(self):
        
        # Crash Handling
        closeProgram = False
        while closeProgram == False:
            
            cv2.namedWindow(self.windowName, cv2.WINDOW_AUTOSIZE)
            self.webcamFeed = cv2.VideoCapture(self.WEBCAM_RTSP_LINK, cv2.CAP_FFMPEG)
            
            print("[DEBUG] [", datetime.now().strftime('%H:%M:%S'), "] Connection to RTSP established")
            
            rval, frame = self.webcamFeed.read()
            
            while rval:
                    
                frame = cv2.resize(frame, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
                    
                cv2.imshow(self.windowName, frame)
                rval, frame = self.webcamFeed.read()
                
                if cv2.waitKey(17) == 27 or cv2.getWindowProperty(self.windowName, cv2.WND_PROP_VISIBLE) < 1:
                    closeProgram = True
                    break
            
            # If program was closed wrongly
            if closeProgram == False:
                print("[ERROR] [", datetime.now().strftime('%H:%M:%S'), "] No Connection to RTSP Stream, reconnecting in 3 seconds. . .")
                sleep(3)
            else:
                print("[DEBUG] Ending RTSP Stream . . .")
                self.webcamFeed.release()
                
                print("[DEBUG] Destroying all open windows . . .")
                cv2.destroyAllWindows()

                print("[DEBUG] Ending program . . .")
                exit()
                    

test = WebcamViewer()