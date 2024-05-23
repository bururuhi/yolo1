from ultralytics import YOLO

# Load a model
model = YOLO("yolov8l.yaml")  # build a new model from scratch
model = YOLO("yolov8l.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model("https://ultralytics.com/images/bus.jpg",save=True)  # predict on an image