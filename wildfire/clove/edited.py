#importing libraries
import urllib.request
import time
import csv
import numpy as np
import pandas as pd
import smtplib


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)


 

def python_sucks():
	




	
	clt, adr = s.accept()
	

	flame = clt.recv(1024).decode()
	print(flame)
	
	
	temp = clt.recv(1024).decode()
	print(temp)
	

	humidity = clt.recv(1024).decode()
	print(humidity)
	

	smoke = clt.recv(1024).decode()
	print(smoke)
	

	soil = clt.recv(1024).decode()
	print(soil)






	dataset = pd.read_csv("data2.csv", error_bad_lines = False)
	x = dataset.iloc[:,:4].values
	y = dataset.iloc[:,4].values



	# encoding of months
	from sklearn.preprocessing import LabelEncoder           
	labelencoder = LabelEncoder()
	x[:, 0] = labelencoder.fit_transform(x[:, 0])



	# splitting of dataset
	from sklearn.model_selection import train_test_split
	x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)



	# applying algorithm
	from sklearn.ensemble import RandomForestClassifier
	classifier1=RandomForestClassifier()
	classifier1.fit(x_train,y_train)
	y_pred=classifier1.predict(x_test)


	# confusion matrix for the testing data
	from sklearn.metrics import confusion_matrix
	cm=confusion_matrix(y_test,y_pred)
	











	x = time.gmtime()[1]
			
	if x==1:
		month="jan"
	elif x==2:
		month="feb"
	elif x==3:
		month="march"
	elif x==4:
		month="april"
	elif x==5:
		month="may"
	elif x==6:
		month="june"
	elif x==7:
		month="july"
	elif x==8:
		month="aug"
	elif x==9:
		month="sept"
	elif x==10:
		month="oct"
	elif x==11:
		month="nov"
	elif x==12:
		month="dec"





	row = []

	row.append(month)
	row.append(soil)
	row.append(temp) 
	row.append(humidity) 

	

				



	try:
		with open("new1.csv",mode =  "r",newline = '') as fp:
			wr = csv.reader(fp, dialect = 'excel')
						

	except FileNotFoundError:
		with open("new1.csv",mode =  "w",newline = '') as fp:
			wr = csv.writer(fp, dialect = 'excel')
			wr.writerow(row)        


	else:
		with open("new1.csv",mode =  "a",newline = '') as fp:
			wr = csv.writer(fp, dialect = 'excel')
			wr.writerow(row) 




					
	#empty file to read x features
	dataset2=pd.read_csv("new1.csv",error_bad_lines=False)
	x_apna=dataset2.iloc[:,:4].values
			
				

	#encoding of first column
	from sklearn.preprocessing import LabelEncoder
	labelencoder = LabelEncoder()

	x_apna[:,0] = labelencoder.fit_transform(x_apna[:,0])
				
	# predicting the probablity
	y_pred1=classifier1 .predict_proba(x_apna)
	prediction = y_pred1[-1]
	print(y_pred1[-1])
	print(type(prediction))
	return prediction

	



	# if prediction > 0.5:
		






	# 	#ML starts here-->>
	# 	import h5py

	# 	import tensorflow as tf 
	# 	import cv2
	# 	import time
	# 	from numpy import loadtxt
	# 	from keras.models import load_model
	# 	tf_classifier = tf.keras.models.load_model('model.h5')
	# 	from keras.models import load_model
	# 	from collections import deque

	# 	import warnings







	# 	warnings.filterwarnings("ignore")

	# 	capture_duration=10
	# 	fire = '0'
	# 	cap = cv2.VideoCapture(1)
	# 	writer = None
	# 	(W, H) = (None, None)
	# 	mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
	# 	Q = deque(maxlen=128)
		
	# 	# loop over frames from the video file stream
	# 	start_time = time.time()
	# 	while (int(time.time() - start_time) < capture_duration):
	# 		# read the next frame from the file
	# 		(grabbed, frame) = cap.read()
		
	# 		# if the frame was not grabbed, then we have reached the end
	# 		# of the stream
	# 		if not grabbed:
	# 			break
		
	# 		# if the frame dimensions are empty, grab them
	# 		if W is None or H is None:
	# 			(H, W) = frame.shape[:2]
	# 		output = frame.copy()
			
	# 		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	# 		frame = cv2.resize(frame, (64,64)).astype("float32")
	# 		frame -= mean
		
	# 		preds = tf_classifier.predict(np.expand_dims(frame, axis=0))[0]
	# 		Q.append(preds)
		
	# 		# perform prediction averaging over the current history of
	# 		# previous predictions
	# 		result = np.array(Q).mean(axis=0)
	# 		i = np.argmax(result)
			
	# 		if result==1:
	# 			head='FIRE'
	# 			print('fire')
	# 			break
	# 			# info = '1'
				
				
			
	# 		else:
	# 			fire = '0'
	# 			head="SAFE"
				
	# 		cv2.putText(output, head, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,1.25, (0, 255, 0), 5)
				
		
	# 		# check if the video writer is None
	# 		if writer is None:
	# 			# initialize our video writer
	# 			fourcc = cv2.VideoWriter_fourcc(*"MJPG")
	# 			writer = cv2.VideoWriter("output", fourcc, 30,(W, H), True)
					
		
	# 		# write the output frame to disk
	# 		writer.write(output)
		
	# 		# show the output image
	# 		cv2.imshow("Output", output)
	# 		key = cv2.waitKey(1) & 0xFF
		
	# 		# if the `q` key was pressed, break from the loop
	# 		if key == ord("q"):
	# 			break

			

		
	# 	cap.release()
	# 	cv2.destroyAllWindows()


	# 	if head == 'FIRE':

	# 		import smtplib

	# 		content = 'fire alert !!'
			

			
	# 		mail = smtplib.SMTP('smtp.gmail.com', 587) 

	# 		mail.ehlo()

	# 		mail.starttls()

	# 		mail.login('bishtshivam096@gmail.com', 'Bisht@123456')

	# 		mail.sendmail('bishtshivam096@gmail.com', 'pranjul41199@gmail.com', content)

	# 		mail.close()

	# 		while True:
	# 			clt, adr = s.accept()
	# 			print(adr)
						
	# 			clt.send(bytes(head, 'utf-8'))  
	# 			break

			



