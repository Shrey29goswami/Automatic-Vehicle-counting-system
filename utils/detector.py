from ultralytics import YOLO
import cv2
# utils/detector.py
class VehicleDetector:
    def __init__(self):
        self.model = YOLO("models/best.pt")

    def detect(self, frame):
        return self.model.predict(frame, conf=0.4, verbose=False)


class PlateDetector:
    def __init__(self):
        self.model = YOLO("models/licence_plate_detection.pt")

    def detect(self, frame):
        return self.model.predict(frame, conf=0.25, verbose=False)