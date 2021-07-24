import urllib.request
import time
import csv
root_url = "192.168.137.72"  # ESP's url, ex: https://192.168.102 (Esp serial prints it when connected to wifi)






class sensor():


	def __init__(self):
		
		self.t = t = 0
		self.h = h = 0
		self.soil = soil = 0
		

#requesing for flame(digital)
	def send_flame_request(self, flame_url):
		
		send_flame_url = urllib.request.urlopen(flame_url) # send request to ESP
		flame_data = send_flame_url.readline()
		f = flame_data.decode()
		print('flame : ', f)

	#requesting for smoke(analog)
	def send_smoke_request(self, smoke_url):

		send_smoke_url = urllib.request.urlopen(smoke_url) # send request to ESP
		smoke_data = send_smoke_url.readline()
		s = smoke_data.decode()
		print('smoke : ', s)

	#requesting for temperature(analog)
	def send_temp_request(self, temp_url):

		send_temp_url = urllib.request.urlopen(temp_url) # send request to ESP
		temp_data = send_temp_url.readline()
		self.t = temp_data.decode()
		print('temp : ', self.t)


	#requesting for humidity(analog)
	def send_humidity_request(self, humidity_url):

		send_humidity_url = urllib.request.urlopen(humidity_url) # send request to ESP
		humidity_data = send_humidity_url.readline()
		self.h = humidity_data.decode()
		print('humidity : ', self.h)		



	#requesting for soil moisture(analog)
	def send_soil_moisture_request(self, soil_moisture_url):

		send_soil_moisture_url = urllib.request.urlopen(soil_moisture_url) # send request to ESP
		soil_moisture_data = send_soil_moisture_url.readline()
		self.soil = soil_moisture_data.decode()
		print('soil_moisture : ', self.soil)





s = sensor()

#infinite loop....
while True:
	
	s.send_flame_request('http://' + root_url + "/flame")
	
		

	s.send_smoke_request('http://' + root_url + "/smoke")
	
		

	s.send_temp_request('http://' + root_url + "/temp")
	
		

	s.send_humidity_request('http://' + root_url + "/humidity")
	
		
	s.send_soil_moisture_request('http://' + root_url + "/soil_moisture")

	
	
	




	x = time.gmtime()[1]
	print(x)
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



	row = [month, s.t, s.h]   

	with open('new1.csv', 'a',newline='',encoding="ISO-8859-1") as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(row)
	csvFile.close()
