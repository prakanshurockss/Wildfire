import h5py
import numpy as np
import tensorflow as tf 
import cv2
import time
from numpy import loadtxt
from keras.models import load_model
classifier = tf.keras.models.load_model('model.h5')
from keras.models import load_model
from collections import deque
import numpy as np
import cv2
import warnings
warnings.filterwarnings("ignore")

capture_duration=10

cap = cv2.VideoCapture(0)
writer = None
(W, H) = (None, None)
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
Q = deque(maxlen=128)
 
# loop over frames from the video file stream
start_time = time.time()
while (int(time.time() - start_time) < capture_duration):
	# read the next frame from the file
    (grabbed, frame) = cap.read()
 
	# if the frame was not grabbed, then we have reached the end
	# of the stream
    if not grabbed:
        break
 
	# if the frame dimensions are empty, grab them
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    output = frame.copy()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (64,64)).astype("float32")
    frame -= mean
  
    preds = classifier.predict(np.expand_dims(frame, axis=0))[0]
    Q.append(preds)
 
	# perform prediction averaging over the current history of
	# previous predictions
    result = np.array(Q).mean(axis=0)
    i = np.argmax(result)
    
    if result==1:
        head='FIRE'
    else:
        head="SAFE"
    cv2.putText(output, head, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,1.25, (0, 255, 0), 5)
		
 
	# check if the video writer is None
    if writer is None:
		# initialize our video writer
	    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
	    writer = cv2.VideoWriter("output", fourcc, 30,(W, H), True)
			
 
	# write the output frame to disk
    writer.write(output)
 
	# show the output image
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
writer.release()
cap.release()
cv2.destroyAllWindows()
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = head
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("alert.mp3") 
  
# Playing the converted file

os.system("start alert.mp3")

