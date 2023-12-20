from sympy import true
import ultralytics
from ultralytics import YOLO
import cv2
import tensorflow as tf
import numpy as np
import os
import shutil
import mediapipe as mp

model_pth=r'C:\Users\HP\OneDrive\Desktop\PranCode\Datasets_Collab\Everything_Needed\yolov8m.pt'
result_pth=r'C:\Users\HP\OneDrive\Desktop\PranCode\Datasets_Collab\Everything_Needed\result'
face_folder_pth=r'C:\Users\HP\OneDrive\Desktop\PranCode\Datasets_Collab\Everything_Needed\Faces'
model=YOLO(model_pth)
current_pred=0                                                                                                                                                                                                          
result_number=1
face_number=1
# shutil.rmtree(result_pth)

hcd=cv2.CascadeClassifier(r'C:\Users\HP\OneDrive\Desktop\PranCode\Datasets_Collab\Everything_Needed\haarcascade_frontalface_default.xml')
def save_faces(img):
    mp_solution=mp.solutions.face_detection
    face_detection = mp_solution.FaceDetection()
    


cap=cv2.VideoCapture(0)
while True:

    _,frame=cap.read()
    results=model.predict(source=frame,show=True,classes=[0])
    for r in results:
        check=len(r.boxes)
        if (check!=0):
            save_faces(frame)
        if (check!=current_pred):
            current_pred=check
            print('now')
            stacked_tensor=r.boxes.xywhn
            for (x,y,w,h) in stacked_tensor:
                x=int(float(x)*640)
                y=int(float(y)*480)
                w=int(float(w)*640)
                h=int(float(h)*480)
                x1=int(x-w/2)
                y1=int(y-h/2)
                cv2.rectangle(frame,pt1=(x1,y1),pt2=(x1+w,y1+h),color=(255,0,0),thickness=2)
                cv2.imwrite(os.path.join(result_pth,f'result_{result_number}.jpg'),frame)
            
        result_number+=1
    # print(check)
    k=cv2.waitKey(1)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()





