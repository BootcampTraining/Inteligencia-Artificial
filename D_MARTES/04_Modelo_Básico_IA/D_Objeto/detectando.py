import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)# utilizar la wecam

majinBooClassif = cv2.CascadeClassifier('cascade.xml')#para utilizar el mdodelo que genera el soft

while True:
	
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	toy = majinBooClassif.detectMultiScale(gray,
	scaleFactor = 9,
	minNeighbors = 91,
	minSize=(70,78))#se convierte la imagen en escala de gris y se guarda en variable toy

	for (x,y,w,h) in toy:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)#dibujar el rectangulo
		cv2.putText(frame,'Majin Boo',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)#colocar el nombre del objeto

	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()