from ultralytics import YOLO
import cv2
from utils.processor import TrafficProcessor

# Load models
vehicle_model = YOLO("models/best.pt")

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    processor = TrafficProcessor()  # 🔥 IMPORTANT

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = vehicle_model(frame)

        # 🔥 Update global counts
        processor.process_vehicles(results)

        annotated_frame = results[0].plot()

        yield annotated_frame  # only frame now

    cap.release()

    # 🔥 FINAL REPORT
    yield processor.get_report()