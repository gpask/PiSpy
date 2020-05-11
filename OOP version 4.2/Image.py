from datetime import datetime
from time import sleep
from picamera import PiCamera
import os

class Image:

    def image_capture(self, folder_name): # take images with pi cam
        cam = PiCamera()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M") #sets variable for current time (to milliseconds)
        sleep(5) # sleep for 10 seconds to let camera "warmup"
        if os.path.exists("/home/pi/" + folder_name):
            if os.getcwd() == ("/home/pi/" + folder_name):
                path = os.getcwd()
            else:
                os.chdir(folder_name)
        else:
            os.mkdir(folder_name)
            os.chdir(folder_name)
        path = os.getcwd()
        cam.capture(path + "/{}.jpg".format(timestamp)) #takes image, saves to specified path with the timestamp as the format
        cam.stop_preview() #hides preview window
        cam.close()
