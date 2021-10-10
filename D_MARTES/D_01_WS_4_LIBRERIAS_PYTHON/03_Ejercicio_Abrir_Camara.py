import cv2
import numpy as np
import imutils
import os
#librerias que se requieren 




cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # para abrir video striming webcam


#__________si deseas colocar rectangulo debes quitar comentarios de las lineas 15,16,24_______
#x1, y1 dibujamos rectangulo en el centro de la Imagen
x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0# variable para guardar varias imagenes
while True:

	ret, frame = cap.read()
	if ret == False:  break
	
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

	
	k = cv2.waitKey(1)
	if k == 27: 
		break

	cv2.imshow('frame',frame)#para cargar la imagen en la cam
	

cap.release()
cv2.destroyAllWindows()