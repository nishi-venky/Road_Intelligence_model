from ultralytics import YOLO

MODEL_PATH = r"D:\runs\detect\vehicle_detection\yolo11n_run\weights\best.pt"

VIDEO_PATH = r"D:\RoadIntelligence\videos\test1.mp4"

TRACKER_PATH = r"C:\Users\Sreelatha\Miniconda3\Lib\site-packages\ultralytics\cfg\trackers\bytetrack.yaml"


# Load model
model = YOLO(MODEL_PATH)


# Run YOLO + ByteTrack
results = model.track(
    source=VIDEO_PATH,
    tracker=TRACKER_PATH,
    persist=True,
    conf=0.25,
    stream=True,
    save=True
)


# Process every frame
for result in results:

    # No tracking IDs in this frame
    if result.boxes.id is None:
        continue

    # Get tracking IDs
    track_ids = result.boxes.id.int().cpu().tolist()

    # Get class IDs
    class_ids = result.boxes.cls.int().cpu().tolist()

    # Get confidence scores
    confidences = result.boxes.conf.cpu().tolist()

    # Get bounding boxes
    boxes = result.boxes.xyxy.cpu().tolist()


    # Process each tracked object
    for track_id, class_id, confidence, box in zip(
        track_ids,
        class_ids,
        confidences,
        boxes
    ):

        class_name = model.names[class_id]

        x1, y1, x2, y2 = box

        print(
            f"ID={track_id} | "
            f"class={class_name} | "
            f"confidence={confidence:.2f} | "
            f"box=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f})"
        )