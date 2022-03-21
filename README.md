# PiSpy: An Affordable, Accessible, and Flexible Imaging Platform for the Automated Observation of Organismal Biology and Behavior

<p align="center">
  <img width="550" src="https://user-images.githubusercontent.com/64978673/158492335-02b7099d-76e5-48fe-99c0-71db24b11269.png">
</p>

This project is licensed under [GNU General Public License v3.0](https://github.com/gpask/PiSpy/blob/master/LICENSE) or any later version\
The hardware is licensed under [CERN-OHL-S v2](https://github.com/gpask/PiSpy/blob/master/Hardware/LICENSE) or any later version\
We are working towards publishing this work! Stay tuned for links to the
BioRxiv and, eventually, full publication.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">PiSpy</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Benjamin I. Morris, Marcy J. Kittredge, Bea Casey, Owen Meng, André Maia Chagas, Matt Lamparter, Thomas Thul, Gregory M. Pask</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br /></a>

**Contents:**
* [Summary](#summary)
* [Overview of the PiSpy](#overview-of-the-pispy)
* [Video and time lapse image recording across various scales](#video-and-time-lapse-image-recording-across-various-scales)
* [Custom setup for monitoring ant behavior](#custom-setup-for-monitoring-ant-behavior)


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

<p align="center">
  <img width="612" alt="Fig. 1" src="https://user-images.githubusercontent.com/64978673/158457158-29e40e41-570e-40ec-b083-b43d4f998991.png">
</p>
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


Imaging of 10 *D. melanogaster* larval locomotion on an agar plate
provided sufficient resolution for analysis with the ImageJ image
processing software, as shown in the above video (sped up to 5x speed):
<p align="center">
  <img width="500" alt="Fig. 2a" src="https://user-images.githubusercontent.com/64978673/158489057-43d25965-56be-4d87-bfe5-761724376ed7.gif">
</p>

Video of crayfish behavior when placed in an aquarium allowed for the
observation of subtle movements of the swimmerets and legs, even though
the animals were underwater and being viewed through a plastic
container:
<p align="center">
  <img width="750" alt="Fig. 2b" src="https://user-images.githubusercontent.com/64978673/158489331-8b840c1c-fed0-4a90-b24e-6aaf5def2067.gif">
</p>

Automated image capture also makes the PiSpy an effective device for
capturing and visualizing organismal growth over time. Time-lapse
imaging every 5 minutes (and converted to a video at 225 fps) of various beans (*Phaseolus vulgaris*) growing in clear
planters showed detailed root and shoot growth:
<p align="center">
  <img width="350" alt="Fig. 2c" src="https://user-images.githubusercontent.com/64978673/158493779-127c2a8b-5336-4cf7-8fa8-4dbde763048f.gif">
</p>

At a smaller scale, imaging every 5 minutes (and converted to a video at 90 fps of the soil bacterium *Bacillus mycoides*
captured the growth and expansion process over time:
<p align="center">
  <img width="500" alt="Fig. 2c" src="https://user-images.githubusercontent.com/64978673/158491507-bb5754b1-c778-42de-97f8-f67b5de99ba1.gif">
</p>

## Custom setup for monitoring ant behavior

<p align="center">
  <img width="278" alt="Fig. 3a" src="https://user-images.githubusercontent.com/64978673/158495407-5360f5aa-5f8d-42fd-b4b4-769b824c158d.png">
</p>

The flexibility of the PiSpy allows it to be customized for more
specific research purposes, as shown above. For example, we have used the PiSpy to
monitor the social behaviors in colonies of the Indian jumping ant,
*Harpegnathos saltator*. Because the ants are housed in nestboxes of a
fixed size, we have modified the wooden frame and mount to enclose the
container to allow for easy overhead recording of the colony, as shown in the image above.
To maintain a light-dark cycle for the ants, we used the LED light
control capabilities of the PiSpy to be able to record social behaviors
throughout the day. Custom LED printed circuit boards (PCBs) can be
connected to the general-purpose input output (GPIO) pin of the
Raspberry Pi and allow for the cycling of white and red lighting.

The sample videos below show the ability of the PiSpy to record animal behavior
in both day and night, with sufficient resolution to capture specific behaviors 
such as antennal dueling (asseen in the daytime recording).
In our experiment, the red light is not detected by the ants but allows
for both day and night imaging. Specific camera settings are used to
record in each different lighting conditions to ensure the desirable
imaging quality. We have programmed in default camera settings for day
and night recording, but the user's manual provides instructions for how
to modify these within the PiSpy code.
<p align="center">
  <img width="500" alt="Fig. 3b" src="https://user-images.githubusercontent.com/64978673/158491840-dfb833ad-e0cf-4621-8a20-a6fd83604eac.gif">
</p>
<p align="center">
  <img width="500" alt="Fig. 3c" src="https://user-images.githubusercontent.com/64978673/158491915-3efa2ea3-894d-4ae9-b964-2cf2e28ca8d8.gif">
</p>

The GPIO pins of the Raspberry Pi can also be used to trigger image or
video capture with an external sensor, such as a motion sensor or IR
break beam. In our setup (below), an ant disrupts the IR beam as it walks to a
foraging arena, and again when it returns to the main colony. The physical setup is 
shown in the image below, including the LEGO contraption to holding the break beam (right side):
<p align="center">
  <img width="522" alt="Fig. 3b" src="https://user-images.githubusercontent.com/64978673/158492397-d180ba2e-1d4e-4796-9bad-11f727a4c1e2.png">
</p>

A sample video in which ants return to the main colony carrying crickets is shown below:
<p align="center">
  <img width="700" alt="Fig. 3c" src="https://user-images.githubusercontent.com/64978673/158492636-761e52c7-627b-4750-a24a-bc5caaa052d7.gif">
</p>

As an alternative to automated recordings at fixed time intervals, triggered recordings such as these
could be used to monitor specific activities, such as feeding patterns
or other behaviors. It is our hope that users will create their own
modifications of the PiSpy hardware and/or software and will share these
for use by other researchers and inspire further customizations,
allowing it to serve as both a general use tool and one that can be
applied to highly specific experimental approaches.

For this README, all videos were converted to GIF using ezgif.com
