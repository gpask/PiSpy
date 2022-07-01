'''
Class for opening and operating the PiSpy GUI
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

from tkinter import *
from datetime import datetime
from Time_Lists import *
from Import_Trigger import *
from Image import *
from picamera import PiCamera
import sched
import time as t

class App:
    
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.master.maxsize(2000, 20000)
        self.resolution = [1280, 720] #default resolution if none selected
        self.framerate = 0 #must be reset if video mode selected
        self._setUpDisplay()
        self._takeAction()
        super(Time_Lists).__init__()


        
    def _takeAction(self):

        def enable_video(): #function to check if video box is checked
            if video.get() %2 != 0:#if video box is checked, enable video setting control
                self.capture_box.config(state = NORMAL)
                self.framerate_box.config(state = NORMAL)
                if timedVideoMode.get() %2 != 0: #if timed video selected
                    self.frequency_box.config(state = NORMAL)
                if triggerVideoMode.get() %2 != 0: #if triggered video selected
                    self.input_trigger_box.config(state = NORMAL)
                    self.delay_box.config(state = NORMAL)
                self.duration_box.config(state = NORMAL)
            else: #otherwise, disable video setting controls
                self.capture_box.config(state = DISABLED)
                self.frequency_box.config(state = DISABLED)
                self.duration_box.config(state = DISABLED)
                self.input_trigger_box.config(state = DISABLED)
                self.delay_box.config(state = DISABLED)
                self.framerate_box.config(state = DISABLED)

        video = IntVar() #creates variable to enable video controls
        self.video_capture_mode = Checkbutton(self.master, text = "Video Capture Mode", variable=video, command=enable_video) #create video check box
        self.video_capture_mode.grid(row=0, column=0, sticky=W) #set location of video check box
        
        def enable_timed_video(): #checks if timed video selected and enables/disables boxes accordingly
            if timedVideoMode.get() %2 != 0 and video.get() %2 != 0:
                self.capture_box.config(state = NORMAL)
                self.frequency_box.config(state = NORMAL)
                self.duration_box.config(state = NORMAL)
            else:
                self.frequency_box.config(state = DISABLED)
        
        timedVideoMode = IntVar() #creates variable to enable timed video mode
        self.timed_video_capture_mode = Checkbutton(self.master, text = "Timed", variable=timedVideoMode, command=enable_timed_video) #create timed video check box
        self.timed_video_capture_mode.grid(row=4, column=0, sticky=W) #set location of timed video check box
        
        def enable_trigger_video(): #checks if triggered video selected and enables/disables boxes accordingly
            if triggerVideoMode.get() %2 != 0 and video.get() %2 != 0:
                self.capture_box.config(state = NORMAL)
                self.duration_box.config(state = NORMAL)
                self.input_trigger_box.config(state = NORMAL)
                self.delay_box.config(state = NORMAL)
            else:
                self.input_trigger_box.config(state = DISABLED)
                self.delay_box.config(state = DISABLED)
        
        triggerVideoMode = IntVar() #creates variable to enable triggered video mode
        self.trigger_video_capture_mode = Checkbutton(self.master, text = "Input Trigger", variable=triggerVideoMode, command=enable_trigger_video) #create input trigger video check box
        self.trigger_video_capture_mode.grid(row=6, column=0, sticky=W) #set location of triggered video check box
     
        def enable_image(): #function to check if image mode is selected
            if image.get() %2 != 0: #image is selected
                if timedImageMode.get() %2 != 0: #timed image is selected
                    self.i_frequency_box.config(state = NORMAL)
                if triggerImageMode.get() %2 != 0: #triggered image is selected
                    self.i_input_trigger_box.config(state = NORMAL)
                    self.i_delay_box.config(state = NORMAL)
                self.i_duration_box.config(state = NORMAL)
            else: #image is not selected
                self.i_frequency_box.config(state = DISABLED)
                self.i_duration_box.config(state = DISABLED)
                self.i_input_trigger_box.config(state = DISABLED)
                self.i_delay_box.config(state = DISABLED)

        image = IntVar() #creates variable to enable image mode
        self.image_capture_mode = Checkbutton(self.master, text = "Image Capture Mode", variable=image, command=enable_image) #creates check box for image mode
        self.image_capture_mode.grid(row=9, column=0, sticky=W) #sets location of image check box
        
        
        def enable_timed_image(): #checks if timed image mode is selected
            if timedImageMode.get() %2 != 0 and image.get() %2 != 0:
                self.i_frequency_box.config(state = NORMAL)
                self.i_duration_box.config(state = NORMAL)
            else:
                self.i_frequency_box.config(state = DISABLED)
        
        timedImageMode = IntVar() #creates variable to enable timed image mode
        self.timed_image_capture_mode = Checkbutton(self.master, text = "Timed", variable=timedImageMode, command=enable_timed_image) #creates check box for timed image mode
        self.timed_image_capture_mode.grid(row=11, column=0, sticky=W) #sets location of check box for timed image mode
        
        def enable_trigger_image(): #checks if triggered image mode is selected
            if triggerImageMode.get() %2 != 0 and image.get() %2 != 0:
                self.i_duration_box.config(state = NORMAL)
                self.i_input_trigger_box.config(state = NORMAL)
                self.i_delay_box.config(state = NORMAL)
            else:
                self.i_input_trigger_box.config(state = DISABLED)
                self.i_delay_box.config(state = DISABLED)
        
        triggerImageMode = IntVar() #creates variable to enable triggered image mode
        self.trigger_video_capture_mode = Checkbutton(self.master, text = "Input Trigger", variable=triggerImageMode, command=enable_trigger_image) #creates check box for triggered image mode
        self.trigger_video_capture_mode.grid(row=13, column=0, sticky=W) #sets location of triggered image mode
           
        def enable_light(): #enables light control boxes if Light Control box is checked
            if light.get() % 2 != 0:
                self.won_box.config(state = NORMAL)
                self.ron_box.config(state = NORMAL)
                self.woff_box.config(state = NORMAL)
                self.roff_box.config(state = NORMAL)
            else:
                self.won_box.config(state = DISABLED)
                self.ron_box.config(state = DISABLED)
                self.woff_box.config(state = DISABLED)
                self.roff_box.config(state = DISABLED)

        light = IntVar() #creates variable to enable light control
        self.light_control = Checkbutton(self.master, text = "Light Control", variable=light, command=enable_light) #creates check box for light control
        self.light_control.grid(row=0, column=4, sticky=W) #positions light control box
        
        def set_resolution(): #sets camera resolution based on selected box
            if resolution1.get() % 2 != 0:
                self.resolution = [1920, 1080]
            elif resolution2.get() % 2 != 0:
                self.resolution = [3280, 2464]
            elif resolution3.get() % 2 != 0:
                self.resolution = [1640, 1232]
            elif resolution4.get() % 2 != 0:
                self.resolution = [1640, 922]
            elif resolution6.get() % 2 != 0:
                self.resolution = [640, 480]
            elif resolution5.get() % 2 != 0:
                self.resolution = [1280, 720]
            else:
                self.resolution = [1280, 720]
        
        resolution1 = IntVar() #along with following lines, creates variables to check for selected resolution
        resolution2 = IntVar()
        resolution3 = IntVar()
        resolution4 = IntVar()
        resolution5 = IntVar()
        resolution6 = IntVar()
        
        
        self.resolution_description = Label(self.master, text= "Select Camera Resolution:").grid(row = 16, column = 0, sticky = W) 
        self.resolution1_box = Checkbutton(self.master, text  = "1920x1080", variable = resolution1, command = set_resolution).grid(row = 17, column = 0, sticky = W) #along with following lines, creates and sets location of resolution check boxes
        self.resolution2_box = Checkbutton(self.master, text  = "3280x2464", variable = resolution2, command = set_resolution).grid(row = 18, column = 0, sticky = W)
        self.resolution3_box = Checkbutton(self.master, text  = "1640x1232", variable = resolution3, command = set_resolution).grid(row = 19, column = 0, sticky = W)
        self.resolution4_box = Checkbutton(self.master, text  = "1640x922", variable = resolution4, command = set_resolution).grid(row = 17, column = 1, sticky = W)
        self.resolution5_box = Checkbutton(self.master, text  = "1280x720", variable = resolution5, command = set_resolution).grid(row = 18, column = 1, sticky = W)
        self.resolution6_box = Checkbutton(self.master, text  = "640x480", variable = resolution6, command = set_resolution).grid(row = 19, column = 1, sticky = W)

        self.framerate_description = Label(self.master, text= "Frame Rate:").grid(row = 2, column = 0, sticky = W)
        self.framerate_description1 = Label(self.master, text="(fps)").grid(row=2, column = 2, sticky = W)
        self.framerate_box = Entry(self.master, state = DISABLED)  #creates framerate selection box
        self.framerate_box.grid(row = 2, column = 1, sticky = W)  #places framerate selection box


        times = Time_Lists() #initiates Time_Lists class
        lights = Day_Night() #initiates Day_Night class

        def set_on(): #sets screen when recording is started
            # disable all buttons and text boxes that can possibly alter program
            self.lock = 0 # initialize to free
            self.apply_button.config(state=DISABLED)
            self.capture_box.config(state=DISABLED)
            self.frequency_box.config(state=DISABLED)
            self.duration_box.config(state=DISABLED)
            time = datetime.now().strftime("%H:%M") # get current system time in hour:minute format
            ID = ''
            if self.filename_box.get() != '':
                ID = self.filename_box.get().replace(" ", "_") + '_'
            if timedImageMode.get() == 1 or timedVideoMode.get() == 1: #timed mode selected
                if video.get() == 1: #timed video mode selected
                    self.times = times.createList(time, float(self.duration_box.get()), ((int(self.frequency_box.get()[0:2])*60) + (int(self.frequency_box.get()[3:5])))) # create list of all recording times
                    self.captureLength = int(self.capture_box.get()[0:2])*60 + int(self.capture_box.get()[3:5]) # record captureLength once initially and store for duration of recordings
                elif image.get() == 1: #timed image mode selected
                    self.image_times = times.createList(time, float(self.i_duration_box.get()), ((int(float(self.i_frequency_box.get()[0:2])*60)) + (int(float(self.i_frequency_box.get()[3:5]))))) # create list of all recording times
                RONTime = self.ron_box.get()
                WONTime = self.won_box.get()
                ROFFTime = self.roff_box.get()
                WOFFTime = self.woff_box.get()
                if video.get() == 1:
                    duration = str(self.duration_box.get())
                    frequency = str(int(self.frequency_box.get()[0:2])*60 + int(self.frequency_box.get()[3:5]))
                    self.framerate = self.framerate_box.get()
                if image.get() == 1:
                    i_duration = str(self.i_duration_box.get())
                    i_frequency = str(int(self.i_frequency_box.get()[0:2])*60 + int(self.i_frequency_box.get()[3:5]))
                root.destroy() #closes GUI window
                if video.get() == 1: #print selected settings
                    print("Chosen settings:")
                    print("Timed Video Mode")
                    print("Clip Length: " + str(self.captureLength) + " seconds")
                    print("Duration: " + duration + " hours")
                    print("Frequency: " + frequency + " minutes")
                    print("Camera Resolution: " + str(self.resolution[0]) + "x" + str(self.resolution[1]))
                    print("Camera Frame Rate: " + str(self.framerate))
                    if ID != '':
                        print("File Identifier: " + ID[:-1])
                    if WONTime != '':
                        print('White lights on at ' + WONTime)
                    if WOFFTime != '':
                        print('White lights off at ' + WOFFTime)
                    if RONTime != '':
                        print('Red lights on at ' + RONTime)
                    if ROFFTime != '':
                        print('Red lights off at ' + ROFFTime)
                    
                    while len(self.times) > 0: #run program with selected settings
                        s = sched.scheduler(t.time, t.sleep)
                        light_thread = s.enter(.5, 1, lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime))
                        time_thread = s.enter(20.25, 1, times.checkVidTime(ID, self.captureLength, self.resolution, self.framerate))
                        
                           
                elif image.get() == 1: #prints selected settings using scheduler
                    print("Chosen settings:")
                    print("Timed Image Mode")
                    print("Duration: " + i_duration + " hours")
                    print("Frequency: " + i_frequency + " minutes")
                    print("Camera Resolution: " + str(self.resolution[0]) + "x" + str(self.resolution[1]))
                    if ID != '':
                        print("File Identifier: " + ID[:-1])
                    if WONTime != '':
                        print('White lights on at ' + WONTime)
                    if WOFFTime != '':
                        print('White lights off at ' + WOFFTime)
                    if RONTime != '':
                        print('Red lights on at ' + RONTime)
                    if ROFFTime != '':
                        print('Red lights off at ' + ROFFTime)
                    
                    while len(self.image_times) > 0: #run program with selected settings using scheduler
                        s = sched.scheduler(t.time, t.sleep)
                        image_light_thread = s.enter(.5, 1, lights.light_on(RONTime, WONTime, ROFFTime, WOFFTime))
                        image_time_thread = s.enter(20.25, 1, times.checkImageTime(ID, self.resolution))
                        
            elif triggerImageMode.get() == 1 or triggerVideoMode.get() == 1: #triggered mode selected
                trigger_mode = Import_Trigger()
                if video.get() == 1: #triggered video selected
                    delay = self.delay_box.get()
                    input_trigger = int(self.input_trigger_box.get())
                    duration = int(self.duration_box.get())
                    length = self.capture_box.get()
                    RONTime = self.ron_box.get()
                    WONTime = self.won_box.get()
                    ROFFTime = self.roff_box.get()
                    WOFFTime = self.woff_box.get()
                    self.framerate = int(self.framerate_box.get())
                    root.destroy() #closes GUI window
                    
                    print("Chosen settings:") #print chosen settings
                    print("Triggered Video Mode")
                    print("Clip Length: " + str(int(length[0:2])*60 + int(length[3:5])) +" seconds")
                    print("Duration: " + str(duration) + " hours")
                    print("Source: GPIO" + str(input_trigger))
                    print("Delay: " + str(int(delay[0:2])*60 + int(delay[3:5])) + " seconds")
                    print("Camera Resolution: " + str(self.resolution[0]) + "x" + str(self.resolution[1]))
                    print("Camera Frame Rate: " + str(self.framerate))
                    if ID != '':
                        print("File Identifier: " + ID[:-1])
                    if WONTime != '':
                        print('White lights on at ' + WONTime)
                    if WOFFTime != '':
                        print('White lights off at ' + WOFFTime)
                    if RONTime != '':
                        print('Red lights on at ' + RONTime)
                    if ROFFTime != '':
                        print('Red lights off at ' + ROFFTime)
                    
                    trigger_mode.video_trigger(ID, delay, input_trigger, duration, length, RONTime, WONTime, ROFFTime, WOFFTime, self.resolution, self.framerate) #run program for triggered video mode
                    
                elif image.get() == 1: #triggered image mode
                    i_delay = self.i_delay_box.get()
                    i_input_trigger = int(self.i_input_trigger_box.get())
                    i_duration = int(self.i_duration_box.get())
                    RONTime = self.ron_box.get()
                    WONTime = self.won_box.get()
                    ROFFTime = self.roff_box.get()
                    WOFFTime = self.woff_box.get()
                    root.destroy() #closes GUI window
                    
                    print("Chosen settings:") #print chosen settings
                    print("Triggered Image Mode")
                    print("Duration: " + str(i_duration) + " hours")
                    print("Source: GPIO" + str(i_input_trigger))
                    print("Delay: " + str(int(i_delay[0:2])*60 + int(i_delay[3:5])) + " seconds")
                    print("Camera Resolution: " + str(self.resolution[0]) + "x" + str(self.resolution[1]))
                    if ID != '':
                        print("File Identifier: " + ID[:-1])
                    if WONTime != '':
                        print('White lights on at ' + WONTime)
                    if WOFFTime != '':
                        print('White lights off at ' + WOFFTime)
                    if RONTime != '':
                        print('Red lights on at ' + RONTime)
                    if ROFFTime != '':
                        print('Red lights off at ' + ROFFTime)
                    
                    trigger_mode.image_trigger(ID, i_delay, i_input_trigger, i_duration, RONTime, WONTime, ROFFTime, WOFFTime, self.resolution) #run program for triggered video mode


                
        self.apply_button = Button(self.master, text = "Run Program", command = set_on)  #creates run program button
        self.apply_button.grid(row=14, column= 5, sticky=W) #places run program buttom
        
        self.filename_description1 = Label(self.master, text="File Identifier:").grid(row=13, column = 4, sticky = E)
        self.filename_box = Entry(self.master)  #creates framerate selection box
        self.filename_box.grid(row = 13, column = 5, sticky = W)  #places framerate selection box

#         def cancel_program(): #allows for changes to parameters
#             # enable all the buttons and boxes disabled when 'Apply' was clicked
#             self.capture_box.delete(0, 'end')
#             self.frequency_box.delete(0, 'end')
#             self.duration_box.delete(0, 'end')
#             self.i_frequency_box.delete(0, 'end')
#             self.i_duration_box.delete(0, 'end')
#             self.won_box.delete(0, 'end')
#             self.ron_box.delete(0, 'end')
#             self.woff_box.delete(0, 'end')
#             self.roff_box.delete(0, 'end')
#             self.capture_box.config(state=DISABLED)
#             self.frequency_box.config(state=DISABLED)
#             self.duration_box.config(state=DISABLED)
#             self.i_frequency_box.config(state=DISABLED)
#             self.i_duration_box.config(state=DISABLED)
#             self.won_box.config(state=DISABLED)
#             self.ron_box.config(state=DISABLED)
#             self.woff_box.config(state=DISABLED)
#             self.roff_box.config(state=DISABLED)
#             self.apply_button.config(state=NORMAL)
#             self.video_capture_mode.deselect()
#             self.image_capture_mode.deselect()
#             self.light_control.deselect()
#             print("Stop button was pressed")
#             #apply_button.cancel(light_on) # cancel apply_button.repeat(500, light_on) 
#             #apply_button.cancel(checkTime) # cancel apply_button.repeat(500, checkTime)
#             lights.whiteLight('off') #turns off light
#             lights.redLight('off') #turns off light

        #self.cancel_button = Button(self.master, text = "Reset", command = cancel_program)
        #self.cancel_button.grid(row=17, column= 5, sticky=W)

        def test_red_light(): #test the camera//used for preview
            lights.redLight('on')
        
        self.red_light_button = Button(self.master, text = "Red Light On", command = test_red_light) 
        self.red_light_button.grid(row=6, column = 5, sticky=W)

        def test_white_light(): #test the camera//used for preview
            lights.whiteLight('on')
       
        self.white_light_button = Button(self.master, text = "White Light On", width = 10, command = test_white_light) 
        self.white_light_button.grid(row=7, column = 5, sticky=W)
        
        def lights_off(): #turns off lights
            lights.whiteLight('off')
            lights.redLight('off')
              
        self.clear_light_button = Button(self.master, text = "Lights Off", width = 10, command = lights_off) 
        self.clear_light_button.grid(row=8, column = 5, sticky=W)
        
        def quick_capture(): #function to capture a single image or video
           if image.get()%2 != 0: #if image is selected, will take a picture
                picture = Image()
                ID = ''
                if self.filename_box.get() != '':
                   ID = self.filename_box.get().replace(" ", "_") + '_'
                picture.image_capture(ID, self.resolution)
                print("picture taken")
           elif video.get()%2 != 0: #if video is selected, will take a video
                capture_length = int(self.capture_box.get()[0:2])*60 + int(self.capture_box.get()[3:5])
                self.framerate = int(self.framerate_box.get())
                recording = Record()
                ID = ''
                if self.filename_box.get() != '':
                    ID = self.filename_box.get().replace(" ", "_") + '_'
                recording.start_record(ID, capture_length, self.resolution, self.framerate)
           else: #if none selected, will say so and not record anything
                print("no mode selected")
                
        self.quick_capture_button = Button(self.master, text = "Quick Capture", width = 10, command = quick_capture)  #creates button for quick capture
        self.quick_capture_button.grid(row=11, column = 5, sticky=W) #places button for quick capture
        
        
        
        def test_cam(): #test the camera//used for preview
            cam = PiCamera()
            if GPIO.input(14) == 1: #if red light is on, use night settings
                if self.resolution == [3280,2464]:#3280x2464 doesnt work for preview so scales down to 1640x1232 which has same field of view
                    lights.camNight(cam, [1640,1232])
                else:    
                    lights.camNight(cam, self.resolution)
            else:#use day settings
                if self.resolution == [3280,2464]:#3280x2464 doesnt work for preview so scales down to 1640x1232 which has same field of view
                    lights.camDay(cam, [1640,1232])
                else:    
                    lights.camDay(cam, self.resolution)
            cam.preview_fullscreen=True #preview screen is not fullscreen
            cam.preview_window=(950, 220, 640, 480) #sets window size for window
            cam.start_preview() #opens preview window
            if self.preview_length_box.get() != '':#if a preview length is specified
                sleep(int(self.preview_length_box.get())) #camera sleeps for specified number of seconds
            else:#if no length specified, default is a 10 second preview
                sleep(10)
            cam.stop_preview() #closes preview window
            cam.close()

        self.preview_button = Button(self.master, text = "Preview Camera", command = test_cam) #creates preview camera button
        self.preview_button.grid(row=10, column = 5, sticky=W) #places preview camera button

    
    def _setUpDisplay(self): #sets up display, creating and placing remaining buttons
        GPIO.setmode(GPIO.BCM) #set BCM GPIO numbering (how pins are referenced)
        GPIO.setwarnings(False) # disables warnings
        GPIO.setup(18,GPIO.OUT) #set GPIO 18 as output (output mode)
        GPIO.setup(14,GPIO.OUT) #set GPIO 14 as output (output mode)
        
        self.preview_length_description = Label(self.master, text= "Preview Length:").grid(row = 10, column = 6, sticky = W)
        self.preview_length_description1 = Label(self.master, text="(seconds)").grid(row=10, column = 8, sticky = W)
        self.preview_length_box = Entry(self.master)
        self.preview_length_box.grid(row = 10, column = 7, sticky = W)
        
        self.capture_description = Label(self.master, text= "Video Clip Length:").grid(row = 1, column = 0, sticky = W)
        self.timecapture_description = Label(self.master, text="(mm:ss)").grid(row=1, column = 2, sticky = W)

        self.frequency_description = Label(self.master, text = "Video Frequency: every").grid(row = 5, column = 0, sticky = W)
        self.timefrequency_description = Label(self.master, text = "(hh:mm)").grid(row = 5, column = 2, sticky = W)

        self.duration_description = Label(self.master, text= "Duration:").grid(row = 3, column = 0, sticky = W)
        self.timeduration_description = Label(self.master, text = "(hours)").grid(row = 3, column = 2, sticky = W)
        
        self.input_description = Label(self.master, text= "Input:").grid(row = 7, column = 0, sticky = W)
        self.triggerinput_description = Label(self.master, text = "(GPIO# (BCM))").grid(row = 7, column = 2, sticky = W)
        
        self.delay_description = Label(self.master, text= "Delay:").grid(row = 8, column = 0, sticky = W)
        self.triggerinput_description = Label(self.master, text = "(mm:ss)").grid(row = 8, column = 2, sticky = W)

        self.capture_box = Entry(self.master, state=DISABLED)
        self.capture_box.grid(row = 1, column = 1, sticky = W)
        self.frequency_box = Entry(self.master, state=DISABLED)
        self.frequency_box.grid(row = 5, column = 1, sticky = W)
        self.duration_box = Entry(self.master, state=DISABLED)
        self.duration_box.grid(row = 3, column = 1, sticky = W)
        self.input_trigger_box = Entry(self.master, state=DISABLED)
        self.input_trigger_box.grid(row = 7, column = 1, sticky = W)
        self.delay_box = Entry(self.master, state=DISABLED)
        self.delay_box.grid(row = 8, column = 1, sticky = W)

        self.i_frequency_description = Label(self.master, text = "Image Frequency: every").grid(row = 12, column = 0, sticky = W)
        self.i_timefrequency_description = Label(self.master, text = "(hh:mm)").grid(row = 12, column = 2, sticky = W)

        self.i_duration_description = Label(self.master, text= "Duration:").grid(row = 10, column = 0, sticky = W)
        self.i_timeduration_description = Label(self.master, text = "(hours)").grid(row = 10, column = 2, sticky = W)
        
        self.i_input_description = Label(self.master, text= "Input:").grid(row = 14, column = 0, sticky = W)
        self.i_triggerinput_description = Label(self.master, text = "(GPIO# (BCM))").grid(row = 14, column = 2, sticky = W)
        
        self.i_delay_description = Label(self.master, text= "Delay:").grid(row = 15, column = 0, sticky = W)
        self.i_triggerinput_description = Label(self.master, text = "(mm:ss)").grid(row = 15, column = 2, sticky = W)

        self.i_frequency_box = Entry(self.master, state=DISABLED)
        self.i_frequency_box.grid(row = 12, column = 1, sticky = W)
        self.i_duration_box = Entry(self.master, state=DISABLED)
        self.i_duration_box.grid(row = 10, column = 1, sticky = W)
        self.i_input_trigger_box = Entry(self.master, state=DISABLED)
        self.i_input_trigger_box.grid(row = 14, column = 1, sticky = W)
        self.i_delay_box = Entry(self.master, state=DISABLED)
        self.i_delay_box.grid(row = 15, column = 1, sticky = W)

        self.light_on_text = Label(self.master, text = "Light Start Times:").grid(row=1, column=4, sticky=W)
        self.light_off_text = Label(self.master, text = "Light Stop Times:").grid(row=1, column=7, sticky=W)

        self.won_box = Entry(self.master, state=DISABLED)
        self.won_box.grid(row = 2, column = 5, sticky=N)
        self.won_box_description = Label(self.master, text= "White LED ON").grid(row=2, column=4, sticky=W)
        self.timewon_description = Label(self.master, text="(hh:mm)").grid(row=2, column=6, sticky=W)

        self.woff_box = Entry(self.master, state=DISABLED)
        self.woff_box.grid(row=2, column=8, sticky= N)
        self.woff_box_description = Label(self.master, text= "White LED OFF").grid(row=2, column=7, sticky=W)
        self.timewoff_description = Label(self.master, text="(hh:mm)").grid(row=2, column=9, sticky=W)

        self.ron_box = Entry(self.master, state=DISABLED)
        self.ron_box.grid(row = 4, column = 5, sticky=N)
        self.ron_box_description = Label(self.master, text= "Red LED ON").grid(row=4, column=4, sticky=W)
        self.timeron_description = Label(self.master, text="(hh:mm)").grid(row=4, column=6, sticky=W)

        self.roff_box = Entry(self.master, state=DISABLED)
        self.roff_box.grid(row=4, column=8, sticky= N)
        self.roff_box_description = Label(self.master, text= "Red LED OFF").grid(row=4, column=7, sticky=W)
        self.timeroff_description = Label(self.master, text="(hh:mm)").grid(row=4, column=9, sticky=W)



root = Tk()
root.geometry("25000x500")

app = App(root, "PiSpy Control")
root.mainloop()
    