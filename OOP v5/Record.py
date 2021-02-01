from datetime import datetime
from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
from Day_Night_Mode import *

class Record:

    def start_record(self, captureLength): # start recording with pi cam, setting camera settings based off which lights are on
        cam = PiCamera()
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
        GPIO.setwarnings(False) # disables warningscam = PiCamera()
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(14,GPIO.OUT) 
        lights = Day_Night()
        if GPIO.input(14) == 1:
            lights.camNight(cam)
        else:
            lights.camDay(cam)
        #el#if GPIO.input(18) == 1:
            #lights.camDay(cam)    
        #print(captureLength)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M") #sets variable for current time (to milliseconds)
        sleep(10) # sleep for 10 seconds to let camera "warmup"
        cam.start_recording("/home/pi/Ant_Vids/Rig1_{}.h264".format(timestamp)) #begins recording, saves to specified path with the timestamp as the format
        cam.wait_recording(captureLength) #checks for exceptions- if error occurs the recording will stop
        cam.stop_recording() #ends the recording. If there is an error it will raise the exception
        cam.stop_preview() #hides preview window
        cam.close()


