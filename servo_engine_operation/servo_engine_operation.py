#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Tue 25 May 2021 15:05:00 CEST
# Author: Charles Auger
# Last updated by: Charles Auger
# Last updated date: Sun 13 Juin 2021 21:22:00 CEST
# Description:
# TP 211 - Solarius
# Scenario 1
# Create a circular arc movement for the solar panel
# with two servo engine 

import time
from adafruit_servokit import ServoKit

def solar_arc(pin1=int, pin2=int):
	'''
	solar_arc is making a circular arc movement to the solar panel

	angles increases of 0.5 degrees vertically and
	of 1 degrees horizontally every 5 seconds

	Parameters (Input Variables):
		-----------
		pin1 : int
			Input the numbers of the digital pin for the vertical servo engine

		pin2 : int
			Input the numbers of the digital pin for the horizontal servo engine

	Output :
		-----------
			Circular movement of the solar panel 

	Dependencies:
        -----------
        In order to use this function, if you copy-paste this function in your code, 
        make sure those 2 modules are properly imported, and properly installed:
            import time
            from adafruit_servokit import ServoKit

	'''
	angle_vertical = 0
	angle_horizontal = 0
	kit = ServoKit(channels=8)
	kit.servo[pin1].angle = 0
	kit.servo[pin2].angle = 0
	while angle_horizontal<=180 :
		angle_vertical += 0.5
		angle_horizontal += 1
		kit.servo[pin1].angle = angle_vertical
		kit.servo[pin2].angle = angle_horizontal
		time.sleep(0.5)

