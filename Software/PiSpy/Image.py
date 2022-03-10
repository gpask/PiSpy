from datetime import datetime
from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
from Day_Night_Mode import *


class Image:

    def image_capture(self, resolution): #captures image, using settings based off which lights are on
        cam = PiCamera()
        lights = Day_Night() #initiates lights class
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced)
        GPIO.setup(18,GPIO.OUT) #tells computer that GPIO pins used for red/white lights are outputs
        GPIO.setup(14,GPIO.OUT) #tells computer that GPIO pins used for red/white lights are outputs
        GPIO.setwarnings(False) # disables warnings
        if GPIO.input(14) == 1: #if red lights are on, use night settings
            lights.camNight(cam, resolution)
        else: #otherwise, use day settings
            lights.camDay(cam, resolution)
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") #sets variable for current time (to minutes)
        sleep(2) # sleep for 2 seconds to let camera "warmup"
        cam.capture("/home/pi/Pictures/{}.jpg".format(timestamp)) #takes image, saves to specified path with the timestamp as the format
        cam.stop_preview() #hides preview window
        cam.close() #closes camera
