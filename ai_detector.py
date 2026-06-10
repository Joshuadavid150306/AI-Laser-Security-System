from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_object(image):

    results = model(image)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls)

            if model.names[cls] == "person":
                return "person"

    return "unknown"
