import cv2 # type: ignore
import numpy as np # type: ignore

# Load YOLO model
net = cv2.dnn.readNet("yolo-cfg/yolov3.weights", "yolo-cfg/yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load COCO names (object classes)
classes = open("yolo-cfg/coco.names").read().strip().split("\n")

def detect_objects(image_path):
    # Load the image from the file path
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    
    # Prepare the image for YOLO
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    
    # Get YOLO output
    outputs = net.forward(output_layers)

    # Initialize variables to store detected objects and traffic counts
    class_ids = []
    confidences = []
    boxes = []
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Dummy logic: Count objects in each quadrant of the image (4 roads)
    road_traffic = {'road_1': 0, 'road_2': 0, 'road_3': 0, 'road_4': 0}
    for i in range(len(boxes)):
        x, y, w, h = boxes[i]
        if x < width // 2 and y < height // 2:
            road_traffic['road_1'] += 1
        elif x >= width // 2 and y < height // 2:
            road_traffic['road_2'] += 1
        elif x < width // 2 and y >= height // 2:
            road_traffic['road_3'] += 1
        else:
            road_traffic['road_4'] += 1
    
    # Return the road with the most traffic
    return max(road_traffic, key=road_traffic.get)
