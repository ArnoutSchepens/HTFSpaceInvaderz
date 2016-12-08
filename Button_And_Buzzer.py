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
            previousInput = button_status
        else:
            digitalWrite(buzzer_pin,0)
            previousInput != button_status
    except KeyboardInterrupt:
        digitalWrite(buzzer_pin, 0)
    except (IOError, TypeError) as e:
        print "Error"
