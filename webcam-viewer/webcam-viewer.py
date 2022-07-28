# Webcam Viewer (& Data Collector + ModelImpl)
# zur Ermoeglichung der Bachelorarbeit

# Livestream und Modelvorhersage von Patrick's Hennenstall
# inkl. dem Eiernest

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

from threading import Event, Thread
from dotenv import load_dotenv
from datetime import datetime
from time import sleep

# Model Implementation
from modelImpl import *

import time
import cv2
import os


class WebcamViewer:

    ### Resolution: 480p ###
    WINDOW_WIDTH     = 854
    WINDOW_HEIGHT    = 480
    
    ### Important Attributes ###
    windowName       = "PatEggAI v0.2 - by Benjamin Hartmann"
    webcamFeed       = None
    WEBCAM_RTSP_LINK = None
    
    stopFlag                  = None
    pauseDataCollectionThread = False
    
    # Debug Flags
    collectData               = False
    showPredictions           = False
    
    def __init__(self):
        
        load_dotenv()
        self.WEBCAM_RTSP_LINK = os.getenv('WEBCAM_RTSP_LINK')
        
        self.__connectHandleWebcamFeed__()
        
    def __startDataCollectionThread__(self):
        self.stopFlag = Event()
        thread = self.DataCollector(self.stopFlag, self)
        thread.start()
    
    def __stopDataCollectionThread__(self):
        self.stopFlag.set()
    
    def __connectHandleWebcamFeed__(self):
        
        # Collection of Data
        if (self.collectData == True):
            self.__startDataCollectionThread__()
        
        # Preparing Object Detector
        detector = FasterRCNNDetector()
        
        # Frame Counter
        i = 1
        
        # Crash Handling
        closeProgram = False
        while closeProgram == False:
            
            cv2.namedWindow(self.windowName, cv2.WINDOW_AUTOSIZE)
            self.webcamFeed = cv2.VideoCapture(self.WEBCAM_RTSP_LINK, cv2.CAP_FFMPEG)
            
            print("[DEBUG] [", datetime.now().strftime('%H:%M:%S'), "] Connection to RTSP established")
            
            startTime = 0
            
            while True:
                
                startTime = time.time()
                rval, frame = self.webcamFeed.read()
                if not rval:
                    break
            
                frame = cv2.resize(frame, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            
                if self.showPredictions == True:
                    frame = detector.webcamDetection(frame)
            
                cv2.imshow(self.windowName, frame)
                
                if self.pauseDataCollectionThread == True:
                    self.pauseDataCollectionThread = False
                
                rval, frame = self.webcamFeed.read()
                
                if cv2.waitKey(17) == 27 or cv2.getWindowProperty(self.windowName, cv2.WND_PROP_VISIBLE) < 1:
                    closeProgram = True
                    break
            
                cv2.setWindowTitle(self.windowName, self.windowName + " (Frame: " + str(i) + " | FPS: " + str(round(1 / (time.time() - startTime))) + ")")
                i += 1
            
            # If program was closed wrongly
            if closeProgram == False:
                print("[ERROR] [", datetime.now().strftime('%H:%M:%S'), "] No Connection to RTSP Stream, reconnecting in 3 seconds. . .")
                cv2.setWindowTitle(self.windowName, self.windowName + " (Reconnecting to RTSP)")
                self.pauseDataCollectionThread = True
                sleep(3)
            else:
                print("[DEBUG] Ending RTSP Stream . . .")
                self.webcamFeed.release()
                
                print("[DEBUG] Destroying all open windows . . .")
                cv2.destroyAllWindows()

                # Stop collecting data
                if (self.collectData == True):
                    self.__stopDataCollectionThread__()

                print("[DEBUG] Ending program . . .")
                break
              
    # Collecting images for Faster-RCNN
    class DataCollector(Thread):
        
        # Initialize Object
        def __init__(self, event, obj):
            self.outerInstance = obj
            Thread.__init__(self) # Start Thread
            self.stopped = event
        
        def run(self):
            
            i = 0
            path = os.path.dirname(os.path.realpath(__file__)) + '\\eggImages\\'
            
            # When re-starting DataCollector, get highest number
            while os.path.exists(path + 'eggSample%s.tiff' % i):
                i += 1
            
            # Repeat this process every 15 minutes
            while not self.stopped.wait(900):
                if self.outerInstance.pauseDataCollectionThread == False:
                    # Retrieve the current frame (.read() returns next frame)
                    rval, frame = self.outerInstance.webcamFeed.retrieve()
                    while frame is None:
                        rval, frame = self.outerInstance.webcamFeed.retrieve()
                    
                    print(path + 'eggSample%s.png' % i)
                    
                    # Write new sample into collection folder
                    cv2.imwrite(path + 'eggSample%s.tiff' % i, frame)
                    print("[DEBUG] [", datetime.now().strftime('%H:%M:%S'), "] Collected new egg sample (Nr.", i, ")")
                    
                    i += 1

# Start Program
test = WebcamViewer()