import time
from grovepi import *
import math

buzzer_pin = 2
button = 4
buzzerOn = False
buttonPrevious = False

pinMode(buzzer_pin, 'OUTPUT')
pinMode(button, 'INPUT')

while True:
    try:
        button_status = digitalRead(button)
        if button_status:
            buttonPrevious = True
        else:
            buttonPrevious = False
        while buttonPrevious != button_status:
            if button_status and buzzerOn == True:
                digitalWrite(buzzer_pin, 0)
                buzzerOn = False
            elif button_status and buzzerOn == False:
                digitalWrite(buzzer_pin, 1)
                buzzerOn = True
    except KeyboardInterrupt:
        digitalWrite(buzzer_pin, 0)
    except (IOError, TypeError) as e:
        print "Error"
