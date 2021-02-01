from Day_Night_Mode import *

class Set_Screen:

    def set_up(self):
        cam = PiCamera()
        cam.camera.preview_fullscreen=False # camera recording preview will not take up full screen
        cam.camera.preview_window=(560, 220, 640, 480) #set up preview window
        cam.camera.start_preview() #calling start_preview() function to begin preview
        if self.nightRecord: # recording during night
            #print("NIGHT")
            cam.camera.exposure_mode = 'nightpreview' #sets exposure mode
            cam.camera.brightness = 60 #set brightness
            cam.camera.awb_mode = 'off' #sets auto-white-balance mode
            cam.camera.awb_gains = (0.4,6) # only has an effect when awb_mode is off // sets auto-white-balance gains
        else: # recording during day
            #print("DAY")
            cam.camera.exposure_mode = 'auto' #sets exposure mode
            cam.camera.brightness = 50 #set brightness
            cam.camera.awb_mode = 'auto' # causes the awb_gains to have no effect // sets auto-white-balance mode 

        cam.close()
