import time
from grovepi import *
import math
import requests
import json

buzzer_pin = 2
button = 4
previousInput = 0
buttonPushed = False
linkAPI = 'http://192.168.50.148:4000/api'
payload = {'team':{'id':13},'sensor':[{'id':0},{'state':True}, {'value', 'WARNING!!!'}]}

pinMode(buzzer_pin, 'OUTPUT')
pinMode(button, 'INPUT')
while True:
    try:
        button_status = digitalRead(button)
        if((button_status) | (NOT(buttonPushed):
            digitalWrite(buzzer_pin,0)
            buttonPushed = False
        else:
            digitalWrite(buzzer_pin,1)
            buttonPushed = True




        """
        button_status = digitalRead(button)
        if ((not previousInput) and button_status):
            digitalWrite(buzzer_pin, 1)
            previousInput = button_status
        else:
            digitalWrite(buzzer_pin,0)
        """
    except KeyboardInterrupt:
        digitalWrite(buzzer_pin, 0)
    except (IOError, TypeError) as e:
        print "Error"
