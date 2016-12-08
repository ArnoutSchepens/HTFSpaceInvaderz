import time
from grovepi import *
import math
import requests

buzzer_pin = 2
button = 4
buzzerOn = False
buttonPrevious = False
linkAPI = 'http://192.168.50.148:4000/api'

pinMode(buzzer_pin, 'OUTPUT')
pinMode(button, 'INPUT')
r = requests.get(linkAPI)
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
