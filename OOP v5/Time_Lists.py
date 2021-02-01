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

    def createList(self, time, hours, freq): #freq in minutes
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
                if (int(currentTime[0:2]) + (int(currentTime[3:]) + freq) // 60) > 23: # if past 24:xx
                    extra = (int(currentTime[0:2]) + (int(currentTime[3:]) + freq) // 60) - 24
                    if extra > 9:
                        hour = str(extra) + ":"
                    else:
                        hour = "0" + str(extra) + ":"
                    currentTime = hour + str(int(currentTime[3:]) - (freq // 60) * 60 + freq) #**THERE SHOULD BE EXTRA CONDITION**
                    if (len(currentTime)==4): #if the minutes over the hour is under 10 eg 00:66
                        currentTime = str((currentTime[0:3])) + "0" + str(int(currentTime[3:])) #set currentTime to be in the new hour with appropriate minutes
                    self.times.append(currentTime) #add time to list of times
                else: #if going to pass xx:59 and not going to pass 24:xx
                    # to fix this scenario: freq > 10 for formatting i.e time = 22:59 and freq = 12 --> 22:011 will be produced
                    '''if (int(currentTime[3:]) - freq //60 + freq) < 10: #if the minutes over the hour is under 10 eg 06:66
                        currentTime = str(int(currentTime[0:2]) + freq // 60) + ":0" + str(int(currentTime[3:]) - (freq // 60) * 60 + freq) #set currentTime to be in the new hour with appropriate minutes
                    else: '''#if the number of minutes over the hour is above 10
                    currentTime = str(int(currentTime[0:2]) + (int(currentTime[3:]) + freq) // 60) + ":" + str(int(currentTime[3:]) - ((int(currentTime[3:]) + freq) // 60) * 60 + freq) #set currentTime to be in the new hour with appropriate minutes
                    # to fix this scenario: currentTime = 00:59 --> 01:59 will be produced instead of 1:59
                    if currentTime[1] is ":": #if the second index of the time string is a colon add a zero in front of first digit
                        currentTime = "0" + currentTime #add zero in front of the currentTime
                    if (len(currentTime)==4): #if the minutes over the hour is under 10 eg 00:66
                        currentTime = str((currentTime[0:3])) + "0" + str(int(currentTime[3:])) #set currentTime to be in the new hour with appropriate minutes
                    self.times.append(currentTime) #add this time to the list of recorded times
            i += 1 #increment i by 1
        print(self.times) #print the list of times to the monitor
        return(self.times) #return it to the computer


    def checkVidTime(self, captureLength): #finds the current time
        time = datetime.now().strftime("%H:%M") # get current system time in hour:minute format
        if time == self.times[0]: # if current system time is next recording time
            del self.times[0] # removes current time from list
            while(self.lock == 1): #while light is on
                print("YA")
                pass;
            self.apply_video_program(captureLength) #call function to start recording
            #print(times)
                
                
    def checkImageTime(self): #finds the current time
        time = datetime.now().strftime("%H:%M") # get current system time in hour:minute format
        if time == self.times[0]:
            del self.times[0]
            while(self.lock==1):
                print("YA")
                pass; 
            self.apply_image_program()


    def apply_video_program(self, captureLength): #helper function to start recording
            recording = Record()
            picture = Image()
            print("Apply button was pressed") #prints to monitor
            recording.start_record(captureLength) #calling start_record function
            print("Recording is finished!") #prints to monitor
                
    def apply_image_program(self): #helper function to start recording
            picture = Image()
            print("Apply button was pressed") #prints to monitor
            print("Image capture has started")
            picture.image_capture()
