from threading import Thread
from dotenv import load_dotenv

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
                
            frame = cv2.resize(frame, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
                
            cv2.imshow(self.windowName, frame)
            rval, frame = self.webcamFeed.read()
            
            if cv2.waitKey(17) == 27 or cv2.getWindowProperty(self.windowName, cv2.WND_PROP_VISIBLE) < 1:
                closeProgram = True
                break
        
        # If program was closed wrongly
        if closeProgram == False:
            # Current Bug: Recursion Error - Fix: Use another loop with closeProgram instead :)
            print("[ERROR] RTSP Stream was closed wrongly, restarting RTSP Stream . . .")
            self.__connectToRTSPStream__()
        else:
            print("[DEBUG] Ending RTSP Stream . . .")
            self.webcamFeed.release()
            
            print("[DEBUG] Destroying all open windows . . .")
            cv2.destroyAllWindows()

            print("[DEBUG] Ending program . . .")
            exit()
            
    def __drawReconnectOnWindow(self):
        pass
        
        

test = WebcamViewer()