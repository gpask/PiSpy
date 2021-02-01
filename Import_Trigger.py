from Image import *
from Record import *
from Day_Night_Mode import *
import RPi.GPIO as GPIO
from datetime import datetime

class Import_Trigger:
    
    def timed_delay(self, delay, RONTime, WONTime, ROFFTime, WOFFTime):
        lights = Day_Night()
        for x in range(delay):
            lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime)
            print(x)
            sleep(1)
    
    def image_trigger(self, delay, trigger, duration, RONTime, WONTime, ROFFTime, WOFFTime):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(trigger, GPIO.IN)
        lights = Day_Night()
        delay = int(delay[0:2])*60 + int(delay[3:5]) #calculates delay in seconds from input string in hh:mm format
        duration = int(duration * 60) #converts duration to minutes
        end_mins = int(datetime.now().strftime("%M")) + duration
        end_hours = int(end_mins // 60) + int(datetime.now().strftime("%H"))
        end_mins = int(end_mins % 60)
        days = 0
        while end_hours >= 24:
            end_hours = end_hours - 24
            days += 1
        end_hours = str(end_hours)
        if len(end_hours) == 1:
            end_hours = '0' + end_hours
        end_mins = str(end_mins)
        if len(end_mins) == 1:
            end_mins = '0' + end_mins
        end_time = end_hours + end_mins
        print(end_time)
        print(days)
        while datetime.now().strftime('%H%M') >= end_time and days != 0:
            if days > 0:
                if datetime.now().strftime('%H%M') == end_time:
                    days = days - 1
                    print('days = ' + str(days))
                    self.timed_delay(60, RONTime, WONTime, ROFFTime, WOFFTime) #need a better way to do this that doesnt pause sensing for a minute
                    
            i = GPIO.input(trigger)
            lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime)
            if i==1: #motion sensor is active
                print('capturing image')
                picture = Image()
                picture.image_capture()
                self.timed_delay(delay, RONTime, WONTime, ROFFTime, WOFFTime)
                print('ready to capture again')
        print('done')
        
    
    def video_trigger(self, delay, trigger, duration, length, RONTime, WONTime, ROFFTime, WOFFTime):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(trigger, GPIO.IN)
        delay = int(delay[0:2])*60 + int(delay[3:5]) #calculates delay in seconds from input string in mm:ss format
        length = int(length[0:2])*60 + int(length[3:5]) #calculates video length in seconds from input string in mm:ss format
        #print(delay)
        lights = Day_Night()
        duration = int(duration * 60) #converts duration to minutes
        end_mins = int(datetime.now().strftime("%M")) + duration
        end_hours = int(end_mins // 60) + int(datetime.now().strftime("%H"))
        end_mins = int(end_mins % 60)
        days = 0
        while end_hours >= 24:
            end_hours = end_hours - 24
            days += 1
        end_hours = str(end_hours)
        if len(end_hours) == 1:
            end_hours = '0' + end_hours
        end_mins = str(end_mins)
        if len(end_mins) == 1:
            end_mins = '0' + end_mins
        end_time = end_hours + end_mins
        print(end_time)
        
        while datetime.now().strftime('%H%M') != end_time and days != 0:
            if days > 0:
                if datetime.now().strftime('%H%M') == end_time:
                    days = days - 1
                    print('days = ' + str(days))
                    self.timed_delay(60, RONTime, WONTime, ROFFTime, WOFFTime) #need a better way to do this that doesnt pause sensing for a minute
            i = GPIO.input(trigger)
            lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime)
            if i==1: #motion sensor is active
                print('capturing video')
                video = Record()
                video.start_record(length)
                print('done recording')
                self.timed_delay(delay, RONTime, WONTime, ROFFTime, WOFFTime)
                print('ready to record again')
                

        