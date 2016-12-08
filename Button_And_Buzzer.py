import time
from grovepi import *
import math

buzzer_pin = 2
button = 4
buzzerOn = False
previousInput = 0

pinMode(buzzer_pin, 'OUTPUT')
pinMode(button, 'INPUT')

while True:
    try:
        button_status = digitalRead(button)
        if ((not previousInput) and button_status):
            digitalWrite(buzzer_pin,1)
            previousInput = button_status
        else:
            digitalWrite(buzzer_pin,0)

    except KeyboardInterrupt:
        digitalWrite(buzzer_pin, 0)
    except (IOError, TypeError) as e:
        print "Error"



"""
        button_status = digitalRead(button)
        if button_status and buzzerOn == True:
            digitalWrite(buzzer_pin, 0)
            buzzerOn = False
        elif button_status and buzzerOn == False:
            digitalWrite(buzzer_pin, 1)
            buzzerOn = True
"""
