import cv2
import numpy as np
from ultralytics import YOLO

# -------------------------------
# 🔹 LOAD MODELS
# -------------------------------

vehicle_model = YOLO('models/best.pt')  # custom trained model for vehicle detectionS
plate_model = YOLO('models/licence_plate_detection.pt')


# -------------------------------
# 🔹 CONFIGURATION
# -------------------------------

heavy_traffic_threshold = 10

vertices1 = np.array([(465, 350), (609, 350), (510, 630), (2, 630)], dtype=np.int32)
vertices2 = np.array([(678, 350), (815, 350), (1203, 630), (743, 630)], dtype=np.int32)

x1, x2 = 325, 635
lane_threshold = 609

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_color = (255, 255, 255)
background_color = (0, 0, 255)


# -------------------------------
# 🔹 VIDEO SETUP
# -------------------------------

cap = cv2.VideoCapture('sample_video1.mp4')

if not cap.isOpened():
    print("ERROR: Could not open video file.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('processed_sample_video1.avi', fourcc, 20.0, (width, height))


# -------------------------------
# 🔹 GLOBAL COUNTERS
# -------------------------------

vehicle_classes = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck"
}

total_counts = {
    "car": 0,
    "motorcycle": 0,
    "bus": 0,
    "truck": 0
}

detected_plates = set()   # stores unique plate detections


# -------------------------------
# 🔹 MAIN LOOP
# -------------------------------

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    detection_frame = frame.copy()

    detection_frame[:x1, :] = 0
    detection_frame[x2:, :] = 0


    # -------------------------------
    # 🔹 VEHICLE DETECTION
    # -------------------------------

    results = vehicle_model.predict(detection_frame, imgsz=640, conf=0.4, verbose=False)

    processed_frame = results[0].plot(line_width=1)

    processed_frame[:x1, :] = frame[:x1, :]
    processed_frame[x2:, :] = frame[x2:, :]

    cv2.polylines(processed_frame, [vertices1], True, (0, 255, 0), 2)
    cv2.polylines(processed_frame, [vertices2], True, (255, 0, 0), 2)

    bounding_boxes = results[0].boxes

    vehicles_in_left_lane = 0
    vehicles_in_right_lane = 0

    vehicle_type_counts = {}


    # -------------------------------
    # 🔹 VEHICLE COUNTING
    # -------------------------------

    for box in bounding_boxes:

        x_min = int(box.xyxy[0][0])
        class_id = int(box.cls[0])
        class_name = vehicle_model.names[class_id]

        vehicle_type_counts[class_name] = vehicle_type_counts.get(class_name, 0) + 1

        if class_name in total_counts:
            total_counts[class_name] += 1

        if x_min < lane_threshold:
            vehicles_in_left_lane += 1
        else:
            vehicles_in_right_lane += 1


    # -------------------------------
    # 🔹 TRAFFIC INTENSITY
    # -------------------------------

    traffic_intensity_left = "Heavy" if vehicles_in_left_lane > heavy_traffic_threshold else "Smooth"
    traffic_intensity_right = "Heavy" if vehicles_in_right_lane > heavy_traffic_threshold else "Smooth"


    # -------------------------------
    # 🔹 LICENSE PLATE DETECTION
    # -------------------------------

    plate_results = plate_model.predict(frame, conf=0.25, verbose=False)

    for plate in plate_results[0].boxes:

        x1p, y1p, x2p, y2p = map(int, plate.xyxy[0])

        cv2.rectangle(processed_frame, (x1p, y1p), (x2p, y2p), (0, 255, 255), 2)
        cv2.putText(processed_frame, "Plate", (x1p, y1p - 10),
                    font, 0.6, (0, 255, 255), 2)

        # store plate location as identifier (since OCR not used yet)
        plate_id = f"{x1p}-{y1p}-{x2p}-{y2p}"
        detected_plates.add(plate_id)


    # -------------------------------
    # 🔹 DISPLAY TEXT INFO
    # -------------------------------

    total_vehicles = sum(vehicle_type_counts.values())

    cv2.rectangle(processed_frame, (10, 10), (600, 140), background_color, -1)

    cv2.putText(processed_frame,
                f'Total Vehicles: {total_vehicles}',
                (20, 40), font, font_scale, font_color, 2)

    cv2.putText(processed_frame,
                f'Left Lane: {vehicles_in_left_lane} ({traffic_intensity_left})',
                (20, 70), font, font_scale, font_color, 2)

    cv2.putText(processed_frame,
                f'Right Lane: {vehicles_in_right_lane} ({traffic_intensity_right})',
                (20, 100), font, font_scale, font_color, 2)


    y_offset = 130
    for v_type, count in vehicle_type_counts.items():
        cv2.putText(processed_frame,
                    f'{v_type}: {count}',
                    (20, y_offset), font, 0.6, (0, 0, 0), 2)
        y_offset += 25


    # -------------------------------
    # 🔹 OUTPUT
    # -------------------------------

    out.write(processed_frame)
    cv2.imshow('Real-time Traffic Analysis', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# -------------------------------
# 🔹 CLEANUP
# -------------------------------

cap.release()
out.release()
cv2.destroyAllWindows()


# -------------------------------
# 🔹 FINAL REPORT
# -------------------------------

print("\n===== FINAL TRAFFIC SUMMARY =====")

total_vehicles_detected = sum(total_counts.values())

print(f"Total Vehicles Detected: {total_vehicles_detected}")

for v_type, count in total_counts.items():
    print(f"{v_type}: {count}")


print("\n===== DETECTED LICENSE PLATES =====")

if detected_plates:
    for i, plate in enumerate(detected_plates, 1):
        print(f"{i}. Plate at region: {plate}")
else:
    print("No plates detected.")