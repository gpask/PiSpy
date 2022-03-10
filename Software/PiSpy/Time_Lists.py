from Image import *
from Record import *

class Time_Lists:

    def __init__(self):
        self.times = list()
        self.image_times = list()
        self.captureLength = int()
        self.lock = int()
        self.duration_min = int()
        self.frequency_min = int()

    def createList(self, time, hours, freq): #function to create list of times for recording, freq is in minutes
        self.times.append(time) #add initial time to list of times
        i = 0 #iterator
        currentTime = time #set the time to an iterable variable
        while i<((hours*(60/freq)-1)): #while i is less than the number of times recorded
            if (int(currentTime[3:]) + freq ) < 60: # if not going to pass xx:59
                currentTime = (currentTime[0:2] + ":" + str((int(currentTime[3:]) + freq))) #make the time a string
                if len(currentTime[3:]) == 1: #check if minutes is single digit
                        currentTime = currentTime[0:3] + "0" + currentTime[3] #add zero before single digit
                self.times.append(currentTime) #add string to the list of times 
            else: # add an hour
                #print(currentTime)
                if (int(currentTime[0:2]) + (int(currentTime[3:]) + freq) // 60) > 23: # if past 24:00
                    extra = (int(currentTime[0:2]) + (int(currentTime[3:]) + freq) // 60) - 24 #calculates how far into the next day the next time is
                    if extra > 9: #if next recording is after 10:00
                        hour = str(extra) + ":"
                    else:
                        hour = "0" + str(extra) + ":" #if hours is a single digit, add leading zero for correct formatting
                    if (int(currentTime[3:]) - (freq // 60) * 60 + freq) >= 60: #if passing 24:00 and minutes also passing xx:59
                        currentTime = hour + str(int(currentTime[3:]) - 60 - (freq // 60) * 60 + freq) #sets next time
                    else: #passing 24:00 but not xx:59
                        currentTime = hour + str(int(currentTime[3:]) - (freq // 60) * 60 + freq) #sets next time
                    if (len(currentTime)==4): #if the minutes over the hour is under 10 eg 00:66, which would be set as 01:6
                        currentTime = str((currentTime[0:3])) + "0" + str(int(currentTime[3:])) #set currentTime to be in the new hour with appropriate minutes (in above example, would be 01:06
                    self.times.append(currentTime) #add time to list of times
                else: #if going to pass xx:59 and not going to pass 24:00
                    currentTime = str(int(currentTime[0:2]) + (int(currentTime[3:]) + freq) // 60) + ":" + str(int(currentTime[3:]) - ((int(currentTime[3:]) + freq) // 60) * 60 + freq) #set currentTime to be in the new hour with appropriate minutes
                    if currentTime[1] is ":": #if the second index of the time string is a colon add a zero in front of first digit
                        currentTime = "0" + currentTime #add zero in front of the currentTime
                    if (len(currentTime)==4): #if the minutes over the hour is under 10 eg 00:66
                        currentTime = str((currentTime[0:3])) + "0" + str(int(currentTime[3:])) #set currentTime to be in the new hour with appropriate minutes
                    self.times.append(currentTime) #add this time to the list of recorded times
            i += 1 #increment i by 1
        #print(self.times) #print the list of times to the monitor
        return(self.times) #return it to the computer


    def checkVidTime(self, captureLength, resolution, framerate): #finds the current time
        time = datetime.now().strftime("%H:%M") # get current system time in hour:minute format
        if time == self.times[0]: # if current system time is next recording time
            del self.times[0] # removes current time from list
            while(self.lock == 1): #while light is on
                pass;
            self.apply_video_program(captureLength, resolution, framerate) #call function to start recording
            #print(times)
                
                
    def checkImageTime(self, resolution): #finds the current time
        time = datetime.now().strftime("%H:%M") # get current system time in hour:minute format
        if time == self.times[0]:
            del self.times[0]
            while(self.lock==1):
                pass; 
            self.apply_image_program(resolution)


    def apply_video_program(self, captureLength, resolution, framerate): #helper function to start recording
            recording = Record()
            picture = Image()
            recording.start_record(captureLength, resolution, framerate) #calling start_record function
            
                
    def apply_image_program(self, resolution): #helper function to start recording
            picture = Image()
            timestamp = datetime.now().strftime("%H:%M") #sets variable for current time (to seconds)
            picture.image_capture(resolution)
