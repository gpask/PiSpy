from datetime import datetime
from time import sleep
from picamera import PiCamera
import os

class Record:

   def start_record(self, captureLength): # start recording with pi cam
        cam = PiCamera() #initialises camera
        timestamp = datetime.now().strftime("%Y%m%d_%H%M") #sets variable for current time (to milliseconds)
        sleep(10) # sleep for 10 seconds to let camera "warmup"
        path = os.getcwd()
        cam.start_recording(path + "/{}.h264".format(timestamp)) #begins recording, saves to specified path with the timestamp as the format
        cam.wait_recording(captureLength) #checks for exceptions- if error occurs the recording will stop
        cam.stop_recording() #ends the recording. If there is an error it will raise the exception
        cam.stop_preview() #hides preview window
        cam.close() #closes camera


