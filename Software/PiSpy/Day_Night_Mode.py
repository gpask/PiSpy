'''
Class controlling day/night cycling and camera settings
Copyright (C) 2022 Benjamin Morris, Marcy Kittredge, Bea Casey, Gregory Pask

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from datetime import datetime
from picamera import PiCamera
from time import sleep
from timeit import Timer
from datetime import datetime
import RPi.GPIO as GPIO


class Day_Night:

    def camDay(self, cam, resolution): #function for daytime camera settings for image recording
        cam.resolution = (resolution) #set resolution of the camera
        cam.framerate = 15 #set the framerate of the camera
        cam.shutter_speed = 40000 #set the shutter speed of the camera
        cam.iso = 200 #set the camera iso (sensitivity of image sensor)
        
    def cam_day(self, cam, resolution, framerate): #function for daytime camera settings for video recording
        cam.resolution = (resolution) #set resolution of the camera
        cam.framerate = int(framerate) #set the framerate of the camera
        cam.shutter_speed = 40000 #set the shutter speed of the camera
        cam.iso = 200 #set the camera iso (sensitivity of image sensor)

    def camNight(self, cam, resolution):  #function for nighttime camera settings for image recording
        cam.resolution = (resolution) #set resolution of the camera
        cam.framerate = 15 #set framerate of the camera
        cam.shutter_speed = 40000 #set the shutter speed of the camera
        cam.brightness = 43 #decrease brightness of camera (improves nighttime image quality)
        cam.contrast = -8 #decrease contrast of camera (improves nighttime image quality)
        cam.iso = 800 #set the camera iso (sensitivity of image sensor)

    def cam_night(self, cam, resolution, framerate):  #function for nighttime camera settings for video recording
        cam.resolution = (resolution) #set resolution of the camera
        cam.framerate = int(framerate) #set framerate of the camera
        cam.shutter_speed = 40000 #set the shutter speed of the camera
        cam.brightness = 43 #decrease brightness of camera (improves nighttime image quality)
        cam.contrast = -8 #decrease contrast of camera (improves nighttime image quality)
        cam.iso = 800 #set the camera iso (sensitivity of image sensor)  
        
    def light_on(self, RONTime, WONTime, ROFFTime, WOFFTime): #helper function for while the light is on
        self.lock = 1; # set lock
        myTime = datetime.now().strftime('%H:%M') # get current time in hour:minute format
        curRONTime = RONTime #red light
        curWONTime = WONTime #white light
        curROFFTime = ROFFTime
        curWOFFTime = WOFFTime
        if myTime == curRONTime: # turn on red light
            sleep(1) #camera sleeps for one second
            self.redLight('on') #turns red light on
            if myTime == curWOFFTime:
                self.whiteLight('off') #turns white light off
        elif myTime == curWONTime: # turn on white light
            sleep(1) #camera sleeps for one second
            self.whiteLight('on') #turns white light on
            if myTime == curROFFTime:
                self.redLight('off') #turns red light off
        elif myTime == curWOFFTime: #turn off white light
            self.whiteLight('off')
        elif myTime == curROFFTime: #turn off red light
            self.redLight('off')
        else: # keep current light on
            pass
        self.lock = 0 # release lock
            

    def whiteLight(self, key): #sets white light
        if key == 'on': #if the function is called to turn light on
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced)
            GPIO.setwarnings(False) # disables warnings
            GPIO.setup(18,GPIO.OUT) #set GPIO 18 as output (output mode)
            GPIO.output(18,GPIO.HIGH) #set to 3.3V
        elif key == 'off': #if the function is called to turn light off
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced)
            GPIO.setwarnings(False) #disables warnings
            GPIO.setup(18,GPIO.OUT) # set GPIO 18 as output (output mode)
            GPIO.output(18,GPIO.LOW) #set to 0V

    def redLight(self, key): #sets red light
        if key == 'on': #if function is called to turn light on
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
            GPIO.setwarnings(False) #disable warnings
            GPIO.setup(14,GPIO.OUT) # set GPIO 14 as output (output mode)
            GPIO.output(14,GPIO.HIGH) #set to 3.3V
        elif key == 'off': #if function is called to turn light off
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
            GPIO.setwarnings(False) #disable warnings
            GPIO.setup(14,GPIO.OUT) #set GPIO as output (output mode)
            GPIO.output(14,GPIO.LOW) #set to 0V