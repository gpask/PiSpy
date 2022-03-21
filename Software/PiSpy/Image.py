'''
Class that controls image capture for the PiSpy
Copyright (C) 2022 Benjamin Morris, Marcy Kittredge, Bea Casey, Gregory Pask

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
