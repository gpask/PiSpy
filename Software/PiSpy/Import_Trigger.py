'''
Class for triggered recording of images or videos
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

from Image import *
from Record import *
from Day_Night_Mode import *
import RPi.GPIO as GPIO
from datetime import datetime
from picamera import PiCamera

class Import_Trigger: #class for triggered recording
    
    def timed_delay(self, delay, RONTime, WONTime, ROFFTime, WOFFTime): #function used to check for lights on/off while delay is happening
        lights = Day_Night() #initiates lights class
        for x in range(delay): #every second for the length of the specified delay, checks if lights need to be switched then sleeps for 1 second 
            lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime)
            sleep(1)
    
    def image_trigger(self, delay, trigger, duration, RONTime, WONTime, ROFFTime, WOFFTime, resolution): #manages sensing and acquisition of images
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) 
        GPIO.setwarnings(False) # disables warnings
        GPIO.setup(trigger, GPIO.IN) # sets GPIO connected to sensor as an input 
        lights = Day_Night() #initiates lights class
        delay = int(delay[0:2])*60 + int(delay[3:5]) #calculates delay in seconds from input string in hh:mm format
        duration = int(duration * 60) #converts duration to minutes
        end_mins = int(datetime.now().strftime("%M")) + duration 
        end_hours = int(end_mins // 60) + int(datetime.now().strftime("%H")) #calculate hour of ending time
        end_mins = int(end_mins % 60) #calculates minutes of ending time (along with line 24
        days = 0
        while end_hours >= 24: #sets number of days during which recording will occur
            end_hours = end_hours - 24
            days += 1
        end_hours = str(end_hours) #recalculates hour of ending time after removing days
        if len(end_hours) == 1:
            end_hours = '0' + end_hours #reformats hours
        end_mins = str(end_mins)
        if len(end_mins) == 1:
            end_mins = '0' + end_mins #reformats minutes
        end_time = end_hours + end_mins #sets end time with correct formatting
        cam = PiCamera() #initates PiCamera. Recording is managed here to avoid camera needing to sleep after being triggered
        if GPIO.input(14) == 1:# if red light is on, use night settings
            lights.camNight(cam, resolution)
        else:# otherwise, use day settings
            lights.camDay(cam, resolution)
        while days >= 0:
            if datetime.now().strftime('%H%M') == end_time: #if reaches end time but there are still 1 or more days remaining, decrease days by 1 
                days = days - 1
                self.timed_delay(60, RONTime, WONTime, ROFFTime, WOFFTime) #delays for 1 minute to prevent loop from running again      
            i = GPIO.input(trigger)
            lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime)
            x =0
            j = 0
            while j < 750: #remove this while loop if using motion sensor. For a break beam, the output is 0 when the beam is broken and 1 when it is not, but the output is not consistent when it should be 1. This loop creates a threshold to prevent accidental activation
                #print(i) #this line can be helpful to make sure the break beam is working correctly (if uncommented, output should be repeatedly printing 1 until break beam is triggered
                x = x + i
                j += 1
                i = GPIO.input(trigger)
            #print(GPIO.input(trigger))
            if x==0: #break beam is broken, for motion sensor switch to if i >= 1 (some sensors output a 1 when triggered and some output a 0, for other sensors test the output by uncommenting the above print statement to determine what to use
                print('capturing image')
                timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") #sets variable for current time (to seconds)
                cam.capture("/home/pi/Pictures/{}.jpg".format(timestamp)) #takes image, saves to specified path with the timestamp as the format
                cam.close() #close camera
                self.timed_delay(delay, RONTime, WONTime, ROFFTime, WOFFTime) #delays specified amount of time, but still checks if lights need to be switched
                cam = PiCamera() #re-opens camera
                if GPIO.input(14) == 1:# if red light is on, use night settings
                    lights.camNight(cam, resolution)
                else:# otherwise, use day settings
                    lights.camDay(cam, resolution)
                print('ready to capture again')
        
    
    def video_trigger(self, delay, trigger, duration, length, RONTime, WONTime, ROFFTime, WOFFTime, resolution, framerate): #manages sensing and acquisition of videos
        
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) 
        GPIO.setwarnings(False) # disables warnings
        GPIO.setup(trigger, GPIO.IN) # sets GPIO connected to sensor as an input 
        lights = Day_Night() #initiates lights class
        delay = int(delay[0:2])*60 + int(delay[3:5]) #calculates delay in seconds from input string in mm:ss format
        length = int(length[0:2])*60 + int(length[3:5]) #calculates video length in seconds from input string in mm:ss format
        duration = int(duration * 60) #converts duration to minutes
        end_mins = int(datetime.now().strftime("%M")) + duration
        end_hours = int(end_mins // 60) + int(datetime.now().strftime("%H")) #calculate hour of ending time
        end_mins = int(end_mins % 60)#calculates minutes of ending time (along with line 24
        days = 0
        while end_hours >= 24: #sets number of days during which recording will occur
            end_hours = end_hours - 24
            days += 1
        end_hours = str(end_hours) #recalculates hour of ending time after removing days
        if len(end_hours) == 1:
            end_hours = '0' + end_hours #reformats hours
        end_mins = str(end_mins)
        if len(end_mins) == 1:
            end_mins = '0' + end_mins #reformats minutes
        end_time = end_hours + end_mins #sets end time with correct formatting
        cam = PiCamera() #initates PiCamera. Recording is managed here to avoid camera needing to sleep after being triggered
        if GPIO.input(14) == 1: # if red light is on, use night settings
            lights.cam_night(cam, resolution, framerate)
        else: #otherwise, use day settings
            lights.cam_day(cam, resolution, framerate)
        while days >= 0:
            if datetime.now().strftime('%H%M') == end_time: #if reaches end time but there are still 1 or more days remaining, decrease days by 1 
                days = days - 1
                self.timed_delay(60, RONTime, WONTime, ROFFTime, WOFFTime) #delays for 1 minute to prevent loop from running again
            i = GPIO.input(trigger)
            lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime)
            x =0
            j = 0
            while j < 750: #remove this while loop if using motion sensor. For a break beam, the output is 0 when the beam is broken and 1 when it is not, but the output is not consistent when it should be 1. This loop creates a threshold to prevent accidental activation
                #print(i) #this line can be helpful to make sure the break beam is working correctly (if uncommented, output should be repeatedly printing 1 until break beam is triggered
                x = x + i
                j += 1
                i = GPIO.input(trigger)
            if x==0: #break beam is broken, for motion sensor switch to if i >= 1 (some sensors output a 1 when triggered and some output a 0, for other sensors test the output by uncommenting the above print statement to determine what to use
                print('capturing video')
                timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") #sets variable for current time (to seconds)
                name = "/home/pi/Videos/{}".format(timestamp)
                cam.start_recording(name + ".h264".format(timestamp)) #begins recording, saves to specified path with the timestamp as the format
                cam.wait_recording(length) #checks for exceptions- if error occurs the recording will stop
                cam.stop_recording() #ends the recording. If there is an error it will raise the exception
                rate = cam.framerate
                cam.close()
                print('done recording')
                os.system("MP4Box -quiet -add //{name}.h264:fps={rate}  //{name}.mp4".format(name = name, rate = rate)) #converts to MP4 using MP4Box. If GPAC cannot be installed, remove this line
                os.remove("//{name}.h264".format(name = name)) #removes .h264 file. If GPAC cannot be installed, remove this line
                self.timed_delay(delay, RONTime, WONTime, ROFFTime, WOFFTime) #delays specified amount of time, but still checks if lights need to be switched
                cam = PiCamera() #re-opens camera
                if GPIO.input(14) == 1: # if red light is on, use night settings
                    lights.cam_night(cam, resolution, framerate)
                else: #otherwise, use day settings
                    lights.cam_day(cam, resolution, framerate)
                print('ready to record again')
                

        
