import cv2
import numpy as np
import imutils
import os
#librerias que se requieren 


Datos = 'n'
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)
 #se crea la carpta "p" para guardar imagenes positivas

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # para abrir video striming webcam

#x1, y1 dibujamos rectangulo en el centro de la Imagen
x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0# variable para guardar varias imagenes
while True:

	ret, frame = cap.read()
	if ret == False:  break
	imAux = frame.copy()#dibuje el recuadro sin borde azul
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)#cargamos el rectangulo en la imagen

	objeto = imAux[y1:y2,x1:x2]#la parte central se guarda en variable
	objeto = imutils.resize(objeto, width=38)#colocar la escala de la imagen en 38
	# print(objeto.shape)
    
	k = cv2.waitKey(1)

  #Si presionamos tecla s guardaremos la imagen en la carpeta 
 #que corresponde la variable datos P, con el nombre de Objeto_   la variable count, 
 #también se imprimirá un mensaje en consola y finalmente aumentamos en 1 el valor 
 #de count para poder seguir almacenando las otras imágenes 
	if k == ord('s'):
		cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
		print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
		count = count + 1
	if k == 27: 
		break

	cv2.imshow('frame',frame)
	cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()