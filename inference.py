import cv2
import pytesseract
from ultralytics import YOLO

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#Else comment it

# Load Model
model = YOLO(r"C:\yolov8\runs\detect\train38\weights\best.pt")


# Run Detection
image_path = r"..\sample_data\image1.jpg"

results = model(image_path)

# Extract Text
image = cv2.imread(image_path)
for r in results:
    for box in r.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        roi = image[y1:y2, x1:x2]
        text = pytesseract.image_to_string(roi)
        print("Detected Text:", text)
