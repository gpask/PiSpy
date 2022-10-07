'''
Class to record videos using the PiSpy
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
from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
from Day_Night_Mode import *
import os as os

class Record:

    def start_record(self, ID, captureLength, resolution, framerate): #captures video, using settings based off which lights are on
        cam = PiCamera()
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced)
        GPIO.setwarnings(False) # disables warnings
        GPIO.setup(18,GPIO.OUT) #tells computer that GPIO pins used for red/white lights are outputs
        GPIO.setup(14,GPIO.OUT) #tells computer that GPIO pins used for red/white lights are outputs
        lights = Day_Night() #initiates lights class
        if GPIO.input(14) == 1: #if red lights are on, use night settings
            lights.cam_night(cam, resolution, framerate)
        else: #otherwise, use day settings
            lights.cam_day(cam, resolution, framerate)
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") #sets variable for current time (to minutes)
        timestamp = ID + timestamp
        sleep(2) # sleep for 2 seconds to let camera "warmup"
        time = datetime.now().strftime("%H:%M:%S") #sets variable for current time (to seconds)
        print("Recording began at " + time) #prints to monitor
        name = "/home/pi/Videos/{}".format(timestamp)
        cam.start_recording(name + ".h264", bitrate = 6000000) #begins recording, saves to specified path with the timestamp as the format. to manually set the bitrate, replace 6000000 with selected value
        cam.wait_recording(captureLength) #checks for exceptions- if error occurs the recording will stop, otherwise records for specified length
        cam.stop_recording() #ends the recording. If there is an error it will raise the exception
        time = datetime.now().strftime("%H:%M:%S") #sets variable for current time (to seconds)
        cam.stop_preview() #hides preview window
        rate = cam.framerate
        cam.close()
        os.system("MP4Box -quiet -add //{name}.h264:fps={rate}  //{name}.mp4".format(name = name, rate = rate)) #converts to MP4 using MP4Box. If GPAC cannot be installed, remove this line
        os.remove("//{name}.h264".format(name = name)) #removes .h264 file. If GPAC cannot be installed, remove this line
        print("Recording is finished!") #prints to monitor


