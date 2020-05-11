from tkinter import *
from datetime import datetime
from Time_Lists import *
from threading import *
from picamera import PiCamera
import sched
import time as t
import os
from Day_Night_Mode import *
import RPi.GPIO as GPIO

class App:

    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.master.maxsize(2000, 20000)

        self._setUpDisplay()
        self._takeAction()
        super(Time_Lists).__init__()

        
    def _takeAction(self):

        def enable_video():
            if video.get() %2 != 0:
                self.capture_box.config(state = NORMAL)
                self.frequency_box.config(state = NORMAL)
                self.duration_box.config(state = NORMAL)
            else:
                self.capture_box.config(state = DISABLED)
                self.frequency_box.config(state = DISABLED)
                self.duration_box.config(state = DISABLED)

        video = IntVar()
        self.video_capture_mode = Checkbutton(self.master, text = "Video Capture Mode", variable=video, command=enable_video)
        self.video_capture_mode.grid(row=0, column=0, sticky=W)
     
        def enable_image():
            if image.get() %2 != 0:
                self.i_frequency_box.config(state = NORMAL)
                self.i_duration_box.config(state = NORMAL)
            else:
                self.i_frequency_box.config(state = DISABLED)
                self.i_duration_box.config(state = DISABLED)

        image = IntVar()
        self.image_capture_mode = Checkbutton(self.master, text = "Image Capture Mode", variable=image, command=enable_image)
        self.image_capture_mode.grid(row=5, column=0, sticky=W)
           
        def enable_light():
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

        light = IntVar()
        self.light_control = Checkbutton(self.master, text = "Light Control", variable=light, command=enable_light)
        self.light_control.grid(row=0, column=4, sticky=W)

        times = Time_Lists()
        lights = Day_Night()

        def cancel_program(): #allows for changes to parameters
            # enable all the buttons and boxes disabled when 'Apply' was clicked
            self.capture_box.delete(0, 'end')
            self.frequency_box.delete(0, 'end')
            self.duration_box.delete(0, 'end')
            self.i_frequency_box.delete(0, 'end')
            self.i_duration_box.delete(0, 'end')
            self.won_box.delete(0, 'end')
            self.ron_box.delete(0, 'end')
            self.woff_box.delete(0, 'end')
            self.roff_box.delete(0, 'end')
            self.capture_box.config(state=DISABLED)
            self.frequency_box.config(state=DISABLED)
            self.duration_box.config(state=DISABLED)
            self.i_frequency_box.config(state=DISABLED)
            self.i_duration_box.config(state=DISABLED)
            self.won_box.config(state=DISABLED)
            self.ron_box.config(state=DISABLED)
            self.woff_box.config(state=DISABLED)
            self.roff_box.config(state=DISABLED)
            self.apply_button.config(state=NORMAL)
            self.video_capture_mode.deselect()
            self.image_capture_mode.deselect()
            self.light_control.deselect()
            print("Stop button was pressed")

        self.cancel_button = Button(self.master, text = "Cancel", command = cancel_program)
        self.cancel_button.grid(row=16, column= 6, sticky=E)

        def set_on(): #sets screen when recording is started
            # disable all buttons and text boxes that can possibly alter program
            self.lock = 0 # initialize to free
            self.cancel_button.config(state=NORMAL)
            time = datetime.now().strftime("%H:%M") # get current system time in hour:minute format
            print('hello')
            #folder = str(self.folder_name)
            #os.mkdir(folder)
            #os.chdir(folder)
            
            if video.get() == 1:
                self.times = times.createList(time, float(self.duration_box.get()),
                                              ((int(self.frequency_box.get()[0:2])*60) +
                                               (int(self.frequency_box.get()[3:5])))) # create list of all recording times
                self.captureLength = int(self.capture_box.get()[0:2])*60 + int(self.capture_box.get()[3:5]) # record captureLength once initially and store for duration of recordings
            elif image.get() == 1:
                self.image_times = times.createList(time, float(self.i_duration_box.get()),
                                                    ((int(self.i_frequency_box.get()[0:2])*60) +
                                                     (int(self.i_frequency_box.get()[3:5])))) # create list of all recording times
            
            if video.get() == 1:
                while len(self.times) > 0:
                    if self.cancel_button == True:
                        cancel_program()
                    s = sched.scheduler(t.time, t.sleep)
                    light_thread = s.enter(.5, 1, lights.light_on(self.ron_box.get(), self.won_box.get(),
                                                                  self.roff_box.get(), self.woff_box.get()))
                    time_thread = s.enter(20.25, 1, times.checkVidTime(self.captureLength))
                       
            elif image.get() == 1:     
                while len(self.image_times) > 0:
                    if self.cancel_button == True:
                        cancel_program()
                    s = sched.scheduler(t.time, t.sleep)
                    image_light_thread = s.enter(.5, 1, lights.light_on(self.ron_box.get(), self.won_box.get(),
                                                                        self.roff_box.get(), self.woff_box.get()))
                    image_time_thread = s.enter(20.25, 1, times.checkImageTime())

            
            
                                  
        self.apply_button = Button(self.master, text = "Apply", command = set_on) 
        self.apply_button.grid(row=16, column= 2, sticky=E)

        
        def test_cam(): #test the camera//used for preview
            cam = PiCamera()
            cam.preview_fullscreen=False #preview screen is not fullscreen
            cam.preview_window=(560, 220, 640, 480) #sets window size for window
            cam.start_preview() #opens preview window
            sleep(5) #camera sleeps for five seconds
            cam.stop_preview() #closes preview window
            cam.close()

        self.preview_button = Button(self.master, text = "Preview Camera", command = test_cam) 
        self.preview_button.grid(row=16, column = 5, sticky=W)

        def test_red_light(): #test the camera//used for preview
            cur_time = datetime.now().strftime("%H:%M")
            if red.get() == 1:
                lights.light_on(cur_time, 0, 0, 0)
            else:
                lights.light_on(0, 0, cur_time, 0)
                
        red = IntVar()
        self.red_light_button = Radiobutton(self.master, text = "Red Light", variable = red, indicatoron = False, width = 8, command = test_red_light) 
        self.red_light_button.grid(row=10, column = 5, sticky=W)

        def test_white_light(): #test the camera//used for preview
            cur_time = datetime.now().strftime("%H:%M")
            if white.get() == 1:
                lights.light_on(0, cur_time, 0, 0)
            else:
                lights.light_on(0, 0, 0, cur_time)
                
        white = IntVar()
        self.white_light_button = Radiobutton(self.master, text = "White Light", variable = white, indicatoron= False, width = 8, command = test_white_light) 
        self.white_light_button.grid(row=13, column = 5, sticky=W)

    
    def _setUpDisplay(self):

        self.capture_description = Label(self.master, text= "Video Clip Length:").grid(row = 1, column = 0, sticky = W)
        self.timecapture_description = Label(self.master, text="(minutes:seconds)").grid(row=1, column = 2, sticky = W)

        self.frequency_description = Label(self.master, text = "Video Frequency: every").grid(row = 2, column = 0, sticky = W)
        self.timefrequency_description = Label(self.master, text = "(hours:minutes)").grid(row = 2, column = 2, sticky = W)

        self.duration_description = Label(self.master, text= "Duration:").grid(row = 3, column = 0, sticky = W)
        self.timeduration_description = Label(self.master, text = "(hours)").grid(row = 3, column = 2, sticky = W)

        self.capture_box = Entry(self.master, state=DISABLED)
        self.capture_box.grid(row = 1, column = 1, sticky = W)
        self.frequency_box = Entry(self.master, state=DISABLED)
        self.frequency_box.grid(row = 2, column = 1, sticky = W)
        self.duration_box = Entry(self.master, state=DISABLED)
        self.duration_box.grid(row = 3, column = 1, sticky = W)

        self.i_frequency_description = Label(self.master, text = "Image Frequency: every").grid(row = 6, column = 0, sticky = W)
        self.i_timefrequency_description = Label(self.master, text = "(hours:minutes)").grid(row = 6, column = 2, sticky = W)

        self.i_duration_description = Label(self.master, text= "Duration:").grid(row = 7, column = 0, sticky = W)
        self.i_timeduration_description = Label(self.master, text = "(hours)").grid(row = 7, column = 2, sticky = W)

        self.i_frequency_box = Entry(self.master, state=DISABLED)
        self.i_frequency_box.grid(row = 6, column = 1, sticky = W)
        self.i_duration_box = Entry(self.master, state=DISABLED)
        self.i_duration_box.grid(row = 7, column = 1, sticky = W)

        self.light_on_text = Label(self.master, text = "Light Start Times:").grid(row=1, column=4, sticky=W)
        self.light_off_text = Label(self.master, text = "Light Stop Times:").grid(row=1, column=7, sticky=W)

        self.won_box = Entry(self.master, state=DISABLED)
        self.won_box.grid(row = 2, column = 5, sticky=N)
        self.won_box_description = Label(self.master, text= "White LED ON").grid(row=2, column=4, sticky=W)
        self.timewon_description = Label(self.master, text="(hours:minutes)").grid(row=2, column=6, sticky=W)

        self.woff_box = Entry(self.master, state=DISABLED)
        self.woff_box.grid(row=2, column=8, sticky= N)
        self.woff_box_description = Label(self.master, text= "White LED OFF").grid(row=2, column=7, sticky=W)
        self.timewoff_description = Label(self.master, text="(hours:minutes)").grid(row=2, column=9, sticky=W)

        self.ron_box = Entry(self.master, state=DISABLED)
        self.ron_box.grid(row = 4, column = 5, sticky=N)
        self.ron_box_description = Label(self.master, text= "Red LED ON").grid(row=4, column=4, sticky=W)
        self.timeron_description = Label(self.master, text="(hours:minutes)").grid(row=4, column=6, sticky=W)

        self.roff_box = Entry(self.master, state=DISABLED)
        self.roff_box.grid(row=4, column=8, sticky= N)
        self.roff_box_description = Label(self.master, text= "Red LED OFF").grid(row=4, column=7, sticky=W)
        self.timeroff_description = Label(self.master, text="(hours:minutes)").grid(row=4, column=9, sticky=W)

        self.folder_name = Entry(self.master)
        self.folder_name.grid(row = 6, column = 5, sticky = W)
        self.folder_name_description = Label(self.master, text = "Folder name").grid(row = 6, column = 4, sticky = W)
        
    
root = Tk()
root.geometry("25000x500")

app = App(root, "Ant Behavioral Recording")    
