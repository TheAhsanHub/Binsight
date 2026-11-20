import cv2
import json
from ultralytics import YOLO

# 1. Load the AI and your JSON Database
model = YOLO("yolo11n.pt")
with open('waste_db . json', 'r') as f:
    waste_db = json.load(f)

cap = cv2.VideoCapture(0)

print("Smart Bin Active... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 2. Run detection
    results = model(frame, conf=0.5)

    for r in results:
        for box in r.boxes:
            # Identify the object
            class_id = int(box.cls[0])
            item_name = model.names[class_id]

            # 3. Check the database
            if item_name in waste_db:
                bin_info = waste_db[item_name]
                instruction = f"Put {item_name} in Bin {bin_info['bin']}"

                # Print instructions to the console
                print(f"{instruction}. {bin_info['message']}")

                # Draw the instruction on the video screen
                cv2.putText(frame, instruction, (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # 4. Show the camera feed
    cv2.imshow("Smart Waste Bin", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()