PiSpy README

# PiSpy: An Affordable, Accessible, and Flexible Imaging Platform for the Automated Observation of Organismal Biology and Behavior

<img width="531" alt="Screen Shot 2022-03-15 at 1 19 32 PM" src="https://user-images.githubusercontent.com/64978673/158434828-18a1521e-5ecc-4b0e-8178-65238707f7d9.png">

This project is licensed under ...

The hardware is licensed under...

We are working towards publishing this work! Stay tuned for links to the
BioRxiv and, eventually, full publication.


Contents:
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

GIF 1 HERE

Imaging of 10 *D. melanogaster* larval locomotion on an agar plate
provided sufficient resolution for analysis with the ImageJ image
processing software, as shown in the above video.

GIF 2 HERE

Video of crayfish behavior when placed in an aquarium allowed for the
observation of subtle movements of the swimmerets and legs, even though
the animals were underwater and being viewed through a plastic
container.

GIF 3 HERE

Automated image capture also makes the PiSpy an effective device for
capturing and visualizing organismal growth over time. Time-lapse
imaging of various beans (*Phaseolus vulgaris*) growing in clear
planters showed detailed root and shoot growth.

GIF 4

At a smaller scale, imaging of the soil bacterium *Bacillus mycoides*
captured the growth and expansion process over time. These time lapses
allow for clear visualization of organismal growth and could be used in
a more formal study to compare and quantify growth of different species
or under different growing conditions.

## Custom setup for monitoring *Harpegnathos saltator* behavior

FIG 3.A HERE

The flexibility of the PiSpy allows it to be customized for more
specific research purposes. For example, we have used the PiSpy to
monitor the social behaviors in colonies of the Indian jumping ant,
*Harpegnathos saltator*. Because the ants are housed in nestboxes of a
fixed size, we have modified the wooden frame and mount to enclose the
container to allow for easy overhead recording of the colony (Fig. 3A).
To maintain a light-dark cycle for the ants, we used the LED light
control capabilities of the PiSpy to be able to record social behaviors
throughout the day. Custom LED printed circuit boards (PCBs) can be
connected to the general-purpose input output (GPIO) pin of the
Raspberry Pi and allow for the cycling of white and red lighting (Fig.
3A).

GIFS of ant videos

In our experiment, the red light is not detected by the ants but allows
for both day and night imaging. Specific camera settings are used to
record in each different lighting conditions to ensure the desirable
imaging quality. We have programmed in default camera settings for day
and night recording, but the user's manual provides instructions for how
to modify these within the PiSpy code.



The GPIO pins of the Raspberry Pi can also be used to trigger image or
video capture with an external sensor, such as a motion sensor or IR
break beam. In our setup, an ant disrupts the IR beam as it walks to a
foraging arena, and again when it returns to the main colony carrying a
cricket (Fig. 3C, S7 Video, S1 Fig.). As an alternative to automated
recordings at fixed time intervals, triggered recordings such as these
could be used to monitor specific activities, such as feeding patterns
or other behaviors. It is our hope that users will create their own
modifications of the PiSpy hardware and/or software and will share these
for use by other researchers and inspire further customizations,
allowing it to serve as both a general use tool and one that can be
applied to highly specific experimental approaches.
