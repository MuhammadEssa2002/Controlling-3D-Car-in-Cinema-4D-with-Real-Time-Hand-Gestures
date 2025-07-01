import cv2
import mediapipe as mp
import time
import math

wCam,hCam = 400,225
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence =0.7)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
cv2.flip

fix,fiy = None,None
tmx,tmy = None,None

while  True:
    sucess, img = cap.read()
    img = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
       
       for handLms in results.multi_hand_landmarks:
           mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
           for id, Lms in enumerate(handLms.landmark):
              h,w,c = img.shape
              cx,cy = (Lms.x*w),(Lms.y*h)
              if id ==0:
                 dir_api = str(Lms.x)
                 with open("api.txt",'w') as f:
                    f.write(dir_api)
              if id == 4:
                 fix,fiy = int(cx) , int(cy)
              if id == 8:
                 tmx,tmy = int(cx), int(cy)
           cv2.circle(img,(fix,fiy),7,(255,255,255),cv2.FILLED)
           cv2.circle(img,(tmx,tmy),7,(255,255,255),cv2.FILLED)
           cv2.line(img,(tmx,tmy),(fix,fiy),(255,255,255),7)
           length = math.hypot(tmx-fix,tmy-fiy)*60/355
           with open("api2.txt",'w') as ff:
              ff.write(str(length))


    cTime = time.time()
    fps = f"Current FPS {int(1/(cTime-pTime))}"
    pTime = cTime
    
    cv2.putText(img,fps,(1,70),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,0))

    cv2.imshow("Image",img)
    cv2.waitKey(1)

