# PiSpy: An Affordable, Accessible, and Flexible Imaging Platform for the Automated Observation of Organismal Biology and Behavior

<img width="491" alt="Screen Shot 2022-03-15 at 8 11 22 PM" src="https://user-images.githubusercontent.com/64978673/158492335-02b7099d-76e5-48fe-99c0-71db24b11269.png">

This project is licensed under ...\
The hardware is licensed under...\
We are working towards publishing this work! Stay tuned for links to the
BioRxiv and, eventually, full publication.


**Contents:**
* [Summary](#summary)
* [Overview of the PiSpy](#overview-of-the-pispy)
* [Video and time lapse image recording across various scales](#video-and-time-lapse-image-recording-across-various-scales)
* [Custom setup for monitoring *Harpegnathos saltator* behavior](#custom-setup-for-monitoring-harpegnathos-saltator-behavior)


## Summary
A great deal of understanding can be gleaned from direct observation of
organismal growth, development, and behavior. However, direct
observation can be time consuming and influence the organism through
unintentional stimuli. Additionally, video capturing equipment can often
be prohibitively expensive, difficult to modify to one's specific needs,
and may come with unnecessary features. Here, we describe the PiSpy, a
low-cost, automated video acquisition platform that uses a Raspberry Pi
computer and camera to record video or images at specified time
intervals or when externally triggered. All settings and controls, such
as programmable light cycling, are accessible to users with no
programming experience through an easy-to-use graphical user.
Importantly, the entire PiSpy system can be assembled for less than
\$100 using laser-cut and 3D-printed components. We demonstrate the
broad applications and flexibility of the PiSpy across a range of model
and non-model organisms. Designs, instructions, and code can be accessed
through an online repository, where a global community of PiSpy users
can also contribute their own unique customizations and help grow the
community of open-source research solutions.

## Overview of the PiSpy
<img width="612" alt="Screen Shot 2022-03-15 at 3 33 50 PM" src="https://user-images.githubusercontent.com/64978673/158457158-29e40e41-570e-40ec-b083-b43d4f998991.png">
Shown above is the base model of the PiSpy for simple image or video
capture (Fig. 1a). A 3D printable holder mounts both the Raspberry Pi
and PiCamera to a laser cut wooden frame, allowing for easy height
adjustment (Fig. 1A-B). The stands on the frame are also reversible, and
a 3D-printed ball and socket mounts the PiCamera, allowing for free
rotation (Fig. 1C). Optionally, the Raspberry Pi computer can connect to
input and/or output components, such as a motion sensor or lighting,
respectively. This entire setup can be assembled for less than \$100, or
cheaper if multiple setups are being bought at once or certain features
are omitted (see Bill of Materials in GitHub. A complete user's guide
and assembly manual can be found in the Supplementary Materials of the
published paper and will also be continually updated on the GitHub
repository (https://github.com/gpask/PiSpy). The GUI for the PiSpy,
written in Python3 using the TKinter package, controls the functionality
of the PiSpy. Features include capture mode, timed or input-triggered
capture, light control, and camera resolution (Fig. 1D). For more
advanced controls, such as changing the default image/video name and
storage location or the specific camera settings, instructions are
written in the user's manual for how to edit these in the code itself.

## Video and time lapse image recording across various scales

![ezgif-5-3c2d1c90c5](https://user-images.githubusercontent.com/64978673/158489057-43d25965-56be-4d87-bfe5-761724376ed7.gif)\
Imaging of 10 *D. melanogaster* larval locomotion on an agar plate
provided sufficient resolution for analysis with the ImageJ image
processing software, as shown in the above video (sped up to 5x speed).


![ezgif-5-1ab624780d](https://user-images.githubusercontent.com/64978673/158489331-8b840c1c-fed0-4a90-b24e-6aaf5def2067.gif)\
Video of crayfish behavior when placed in an aquarium allowed for the
observation of subtle movements of the swimmerets and legs, even though
the animals were underwater and being viewed through a plastic
container.

![ezgif-5-a99b9cc39b](https://user-images.githubusercontent.com/64978673/158490145-afa4f2dd-aa33-4e09-8ed2-d727756cef79.gif)\
Automated image capture also makes the PiSpy an effective device for
capturing and visualizing organismal growth over time. Time-lapse
imaging every 5 minutes (and converted to a video at 300 fps) of various beans (*Phaseolus vulgaris*) growing in clear
planters showed detailed root and shoot growth.

![ezgif-5-3105a73d64](https://user-images.githubusercontent.com/64978673/158491507-bb5754b1-c778-42de-97f8-f67b5de99ba1.gif)\
At a smaller scale, imaging every 5 minutes of the soil bacterium *Bacillus mycoides*
captured the growth and expansion process over time. These time lapses (converted to a video at 90 fps)
allow for clear visualization of organismal growth and could be used in
a more formal study to compare and quantify growth of different species
or under different growing conditions.

## Custom setup for monitoring *Harpegnathos saltator* behavior


<img width="280" alt="Screen Shot 2022-03-15 at 8 02 36 PM" src="https://user-images.githubusercontent.com/64978673/158491664-8bef87b2-deb3-4322-8f3f-afb618bd6aa6.png">\
The flexibility of the PiSpy allows it to be customized for more
specific research purposes. For example, we have used the PiSpy to
monitor the social behaviors in colonies of the Indian jumping ant,
*Harpegnathos saltator*. Because the ants are housed in nestboxes of a
fixed size, we have modified the wooden frame and mount to enclose the
container to allow for easy overhead recording of the colony, as shown in the image above.
To maintain a light-dark cycle for the ants, we used the LED light
control capabilities of the PiSpy to be able to record social behaviors
throughout the day. Custom LED printed circuit boards (PCBs) can be
connected to the general-purpose input output (GPIO) pin of the
Raspberry Pi and allow for the cycling of white and red lighting.


![ezgif-5-b6089be5c8](https://user-images.githubusercontent.com/64978673/158491840-dfb833ad-e0cf-4621-8a20-a6fd83604eac.gif)
![ezgif-5-17523869d1](https://user-images.githubusercontent.com/64978673/158491915-3efa2ea3-894d-4ae9-b964-2cf2e28ca8d8.gif)\
These sample videos show the ability of the PiSpy to record animal behavior
in both day and night, with sufficient resolution to capture specific behaviors 
such as antennal dueling (seen in the daytime recording)
In our experiment, the red light is not detected by the ants but allows
for both day and night imaging. Specific camera settings are used to
record in each different lighting conditions to ensure the desirable
imaging quality. We have programmed in default camera settings for day
and night recording, but the user's manual provides instructions for how
to modify these within the PiSpy code.


<img width="522" alt="Screen Shot 2022-03-15 at 8 08 45 PM" src="https://user-images.githubusercontent.com/64978673/158492397-d180ba2e-1d4e-4796-9bad-11f727a4c1e2.png"> \
![ezgif-5-ce08846a2f](https://user-images.githubusercontent.com/64978673/158492636-761e52c7-627b-4750-a24a-bc5caaa052d7.gif)

The GPIO pins of the Raspberry Pi can also be used to trigger image or
video capture with an external sensor, such as a motion sensor or IR
break beam. In our setup, an ant disrupts the IR beam as it walks to a
foraging arena, and again when it returns to the main colony carrying a
cricket (seen in the sample video). The physical setup is 
shown in the image above, including the LEGO contraption to holding the break beam (right side).

As an alternative to automatedrecordings at fixed time intervals, triggered recordings such as these
could be used to monitor specific activities, such as feeding patterns
or other behaviors. It is our hope that users will create their own
modifications of the PiSpy hardware and/or software and will share these
for use by other researchers and inspire further customizations,
allowing it to serve as both a general use tool and one that can be
applied to highly specific experimental approaches.

For this README, all videos were converted to GIF using ezgif.com
