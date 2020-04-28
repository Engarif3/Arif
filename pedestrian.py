import cv2
import time

video_src = 'pedestrians.avi'
cap = cv2.VideoCapture(video_src)

fcount = 0

cascade = cv2.CascadeClassifier('cascade.xml')

while True:
    
        ret, img = cap.read()
        
	if (type(img) == type(None)):
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pedestrian = cascade.detectMultiScale(gray, 2.4,7)
        font = cv2.FONT_HERSHEY_SIMPLEX
        

        for (a, b, c, d) in pedestrian:
            cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 1)
            cv2.putText(img, 'Pedestrian', (a, b), font, 0.5, (0, 0, 200), 1)

        cv2.imshow('video', img)

        if cv2.waitKey(33) == 27:
            break

  

cv2.destroyAllWindows()
