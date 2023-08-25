from ultralytics import YOLO
import cv2
import math
from helper import create_video_writer

cap = cv2.VideoCapture('videos/ppe-2.mp4')
writer = create_video_writer(cap, "ConstructionSiteSafetyOutput.mp4")

model = YOLO("best.pt")

classNames = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest',
              'Person', 'SUV', 'Safety Cone', 'Safety Vest', 'bus', 'dump truck', 'fire hydrant', 'machinery',
              'mini-van', 'sedan', 'semi', 'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']
myColor = (0, 0, 255)
while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            print(currentClass)
            if conf > 0.5:
                if currentClass =='NO-Hardhat' or currentClass =='NO-Safety Vest' or currentClass == "NO-Mask":
                    myColor = (0, 0,255)
                elif currentClass =='Hardhat' or currentClass =='Safety Vest' or currentClass == "Mask":
                    myColor =(0,255,0)
                else:
                    myColor = (255, 0, 0)


                image = cv2.putText(img, f'{classNames[cls]}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

    cv2.imshow("Image", img)
    writer.write(img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()
#cv2.waitKey(1)