import RPi.GPIO as GPIO
import os
import time
#from RPi.GPIO import GPIO


#LBO shutdown PIN

PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Check for low power
while True:

	if not GPIO.input(PIN):
 # logger.debug("Low Battery Power Detected.  Shutting down...")
 # GCD.off()
 # os.system("sudo shutdown -h now")
		print ("powering down")
		time.sleep(1)

	else:
		print ("all good")
		time.sleep(1)
