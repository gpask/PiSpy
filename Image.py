from datetime import datetime
from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
from Day_Night_Mode import *

class Image:

    def image_capture(self): # take images with pi cam, setting camera settings based off which lights are on
        cam = PiCamera()
        lights = Day_Night()
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
        GPIO.setwarnings(False) # disables warningscam = PiCamera()
        if GPIO.input(14) == 1:#  or ((GPIO.input(14) == 0 and GPIO.input(18) == 0)):
            lights.camNight(cam)
        else:# GPIO.input(18) == 1:
            lights.camDay(cam)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M") #sets variable for current time (to milliseconds)
        sleep(10) # sleep for 10 seconds to let camera "warmup"
        cam.capture("/home/pi/Ant_Pictures/Rig1_{}.jpg".format(timestamp)) #takes image, saves to specified path with the timestamp as the format
        cam.stop_preview() #hides preview window
        cam.close()
