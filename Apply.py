from Image import *
from Record import *

class Apply:

    def apply_program(self, video, image, captureLength): #helper function to start recording
            recording = Record()
            picture = Image()
            print("Apply button was pressed") #prints to monitor
            if video % 2 == 1:
                recording.start_record(captureLength) #calling start_record function
                print("Recording is finished!") #prints to monitor
            elif image % 2 == 1:
                print("Image capture has started")
                picture.image_capture()
    

