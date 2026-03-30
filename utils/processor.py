# utils/processor.py

class TrafficProcessor:
    def __init__(self):
        self.total_count = 0
        self.class_counts = {}
        self.detected_plates = set()

    def process_vehicles(self, results):
        for box in results[0].boxes:
            class_name = results[0].names[int(box.cls[0])]

            self.class_counts[class_name] = self.class_counts.get(class_name, 0) + 1
            self.total_count += 1

    def process_plates(self, plate_results):
        for plate in plate_results[0].boxes:
            x1, y1, x2, y2 = map(int, plate.xyxy[0])
            plate_id = f"{x1}-{y1}-{x2}-{y2}"

            self.detected_plates.add(plate_id)

    def get_report(self):
        return {
            "total": self.total_count,
            "classes": self.class_counts,
            "plates": list(self.detected_plates)
        }