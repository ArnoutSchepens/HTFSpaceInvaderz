import time
from grovepi import *
import math
import requests

buzzer_pin = 2
button = 4
buzzerOn = False
previousInput = 0
linkAPI = 'http://192.168.50.148:4000/api'

pinMode(buzzer_pin, 'OUTPUT')
pinMode(button, 'INPUT')
r = requests.post(linkAPI, data = {'team':{{'id' : 13}}, 'sensor':{{'id': 0}, {'state':True}, {'value':'WARNING!'}}})
print(r.url)
while True:
    try:
        button_status = digitalRead(button)
        if ((not previousInput) and button_status):
            digitalWrite(buzzer_pin, 1)
            previousInput = button_status
        else:
            digitalWrite(buzzer_pin,0)
    except KeyboardInterrupt:
        digitalWrite(buzzer_pin, 0)
    except (IOError, TypeError) as e:
        print "Error"
