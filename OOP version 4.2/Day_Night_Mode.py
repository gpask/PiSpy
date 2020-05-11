from datetime import datetime
from picamera import PiCamera
from time import sleep
from timeit import Timer
from datetime import datetime
import RPi.GPIO as GPIO


class Day_Night:
    
    def __init__(self):
        self.nightRecord = False

    def camDay(self):
        cam = PiCamera() #initialise camera
        self.nightRecord = False #set nightRecord to False --> indicates daytime recording
        cam.resolution = (1640, 1232) #set resolution of the camera
        cam.framerate = 40 #set the framerate of the camera
        cam.shutter_speed = 10000000 #set the shutter speed of the camera
        cam.iso = 100 #set the camera iso (sensitivity of image sensor)
        cam.exposure_mode = 'auto' #sets exposure mode
        cam.brightness = 50 #set brightness
        cam.awb_mode = 'auto' # causes the awb_gains to have no effect // sets auto-white-balance mode 
        cam.close()

    def camNight(self):
        cam = PiCamera() #initialise camera
        self.nightRecord = True #set nightRecord to True --> indicates nighttime recording
        cam.resolution = (1280, 720) #set resolution of the camera
        cam.framerate = 40 #set framerate of the camera
        cam.shutter_speed = 0 #10000000 #set the shutter speed of the camera (auto)
        cam.iso = 800 #set the camera iso (sensitivity of image sensor)
        cam.exposure_mode = 'night' #sets exposure mode
        cam.saturation = -100 #lower saturation of red light
        cam.brightness = 30 #set brightness
        cam.awb_mode = 'off' #sets auto-white-balance mode
        cam.awb_gains = (0.4,6) # only has an effect when awb_mode is off // sets auto-white-balance gains
        cam.close()

    def light_on(self, RONTime, WONTime, ROFFTime, WOFFTime): #helper function for while the light is on
        self.lock = 1; # set lock
        myTime = datetime.now().strftime('%H:%M') # get current time in hour:minute format
        curRONTime = RONTime #+ ':00' //red light
        curWONTime = WONTime #+ ":00" //white light
        curROFFTime = ROFFTime
        curWOFFTime = WOFFTime
        if myTime == curRONTime: # turn on red light
            sleep(1) #camera sleeps for one second
            self.redLight('on') #turns red light on
            if myTime == curWOFFTime:
                self.whiteLight('off') #turns white light off
            self.camNight() # set camera to night mode
        elif myTime == curWONTime: # turn on white light
            sleep(1) #camera sleeps for one second
            self.whiteLight('on') #turns white light on
            if myTime == curROFFTime:
                self.redLight('off') #turns red light off
            self.camDay() # set camera to day mode
        elif myTime == curWOFFTime:
            self.whiteLight('off') #turns white light off
        elif myTime == curROFFTime:
            self.redLight('off') #turns white light off
        else: # keep current light on
            pass
        self.lock = 0 # release lock
            

    def whiteLight(self, key): #sets white light
        if key is 'on': #if the function is called to turn light on
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
            GPIO.setwarnings(False) # disables warnings
            GPIO.setup(18,GPIO.OUT) #set GPIO 18 as output (output mode)
            GPIO.output(18,GPIO.HIGH) #set to 3.3V
        elif key is 'off': #if the function is called to turn light off
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
            GPIO.setwarnings(False) #disables warnings
            GPIO.setup(18,GPIO.OUT) # set GPIO 18 as output (output mode)
            GPIO.output(18,GPIO.LOW) #set to 0V

    def redLight(self, key): #sets red light
        if key is 'on': #if function is called to turn light on
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
            GPIO.setwarnings(False) #disable warnings
            GPIO.setup(14,GPIO.OUT) # set GPIO 14 as output (output mode)
            GPIO.output(14,GPIO.HIGH) #set to 3.3V
        elif key is 'off': #if function is called to turn light off
            GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced) **CHANGE TO GPIO.BOARD- SAFER**
            GPIO.setwarnings(False) #disable warnings
            GPIO.setup(14,GPIO.OUT) #set GPIO as output (output mode)
            GPIO.output(14,GPIO.LOW) #set to 0V
