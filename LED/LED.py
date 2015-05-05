"""
A program for blinking an LED light on pin 7 of a Raspberry Pi. 
Created By: Asad Zia
"""

import RPi.GPIO as GPIO  
import time  
  
def blink(pin):  
    # to use Raspberry Pi board pin numbers  
    GPIO.setmode(GPIO.BOARD)  
	# set up GPIO output channel  
    GPIO.setup(7, GPIO.OUT)  
		
    blinks = input("Please enter the number of blinks: ")
    duration = input("Please enter the duration between blinks: ")

    for i in range (0, blinks):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(duration)  
        GPIO.output(pin, GPIO.LOW)  
        time.sleep(duration)  
    # Cleaning up
    GPIO.cleanup() 
    return  

# Testing the blink function
blink(7);
