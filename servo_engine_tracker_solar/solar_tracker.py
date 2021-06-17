#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Tue 25 May 2021 15:05:00 CEST
# Author: Charles Auger
# Last updated by: Charles Auger
# Last updated date: Sun 13 Juin 2021 21:22:00 CEST
# Description:
# TP 212 - Solarius
# Scenario 2
# Create a movement for the solar panel to track the sun
# with two servo engine and
# four sensors

import time
from adafruit_servokit import ServoKit
from adafruit_circuitplayground.express import cpx

angle_vertical = 0
angle_horizontal = 0


def move_up(pin1=int):
	"""
	move_up is move up the solar panel of 0.5 degrees

	Parameters (Input Variables):
		-----------
		pin1 : int
			Input the numbers of the digital pin for the vertical servo engine

	Output :
		----------
		move up the solar panel of 0.5 degrees 
	"""
	angle_vertical += 0.5
	kit.servo[pin1].angle = angle_vertical
	

def move_down(pin1=int):
	"""
	move_down is move down the solar panel of 0.5 degrees

	Parameters (Input Variables):
		-----------
		pin1 : int
			Input the numbers of the digital pin for the vertical servo engine

	Output :
		----------
		move down the solar panel of 0.5 degrees 
	"""
	angle_vertical -= 0.5
	kit.servo[pin1].angle = angle_vertical


def move_right(pin2=int):
	"""
	move_right is move right the solar panel of 1 degrees

	Parameters (Input Variables):
		-----------
		pin2 : int
			Input the numbers of the digital pin for the horizontal servo engine

	Output :
		----------
		move right the solar panel of 1 degrees 
	"""
	angle_horizontal -= 1
	kit.servo[pin2].angle = angle_horizontal


def move_left(pin2=int):
	"""
	move_left is move left the solar panel of 1 degrees

	Parameters (Input Variables):
		-----------
		pin2 : int
			Input the numbers of the digital pin for the horizontal servo engine

	Output :
		----------
		move left the solar panel of 1 degrees
	"""
	angle_horizontal += 1
	kit.servo[pin2].angle = angle_horizontal


def light_measure(pin3=int):
	"""
	light_measure measures the light fron the sensor of the cpx

	Parameters (Input Variables):
		-----------
		pin3 : int
			Input the numbers of the analog pin for the cpx

	output : 
		---------
		Light pixel : int
		Output the value of the light from the sensor 
		every seconds
	"""
cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.3

while True:
	# light value remapped to pixel position
	peak = simpleio.map_range(cpx.light, 0, 320, 0, 10)
	print(cpx.light)
	print(int(peak))

	if cpx.pixels[pin3] <= peak:
		cpx.pixels[pin3] = (0, 255, 255)
	else:
		cpx.pixels[pin3] = (0, 0, 0)
    cpx.pixels.show()
    time.sleep(1)
    return cpx.pixels[pin3]


def solar_tracker(pin1=int, pin2=int, pin3=int):
	"""
	main function 
	solar_tracker moves the solar panels to track the sun

	Parameters (Input Variables):
		-----------
		pin1 : int
			Input the numbers of the digital pin for the vertical servo engine

		pin2 : int
			Input the numbers of the digital pin for the horizontal servo engine

	Output :
		-----------
		movement of the solar panel in function of the position of the light

	Dependencies:
        -----------
        In order to use this function, if you copy-paste this function in your code, 
        make sure those 3 modules are properly imported, and properly installed:
            import time
            from adafruit_servokit import ServoKit
            from adafruit_circuitplayground.express import cpx

	"""
	while True :
		light_measure(pin3=int)=light
		if light > 240:
			move_up(pin1=int)

		elif light > 160 and light <= 240 :
			move_down(pin1=int)
		elif light > 80 and light <= 160 :
			move_right(pin2=int)
		else :
			move_left(pin2=int)




