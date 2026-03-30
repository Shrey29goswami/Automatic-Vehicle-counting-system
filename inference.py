from ultralytics import YOLO

# load once (important for performance)
model = YOLO("models/best.pt")

def detect(frame):
    results = model(frame)
    return results