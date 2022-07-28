# ModelImpl
# zur Ermoeglichung der Bachelorarbeit

# Modelvorhersage von Eiern im Eiernest

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer

import pickle

class FasterRCNNDetector:
    
    # Instanziierungsmethode
    def __init__(self):
        
        # Laden der Modell Konfiguration
        with open("./model/model_cfg.pickle", 'rb') as f:
            self.cfg = pickle.load(f)
        
        # Laden des Modells und Konfigurationen
        self.cfg.MODEL.WEIGHTS = "./model/output/model_final.pth"
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5 # Vorhersage Threshold
        self.cfg.MODEL.DEVICE = "cpu"

        # Instanziierung der Vorhersageklasse
        self.predictor = DefaultPredictor(self.cfg)
        
        # Setzen der Metadaten fuer Anzeige
        self.metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0])
        self.metadata.set(thing_classes=self.cfg.MODEL.THINGCLASSES)
       
    # Erkennung der Objekte in einem Bild 
    def webcamDetection(self, frame):
        
        # Vorhersage der Objekte
        predictions = self.predictor(frame)
        
        # Visualisierung der gefundenen Objekte
        visualizer = Visualizer(frame[:,:,::-1], metadata = self.metadata, instance_mode = ColorMode.IMAGE)
        output = visualizer.draw_instance_predictions(predictions["instances"].to("cpu"))
        
        return output.get_image()[:,:,::-1]