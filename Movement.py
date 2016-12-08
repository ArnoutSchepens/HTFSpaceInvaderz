import time
from grovepi import *
import math
import requests
import json
from grove_rgb_lcd import *

class movement:

    ultrasonic_ranger = 3
    button = 4
    linkAPI = 'http://192.168.50.148:4000/api'
    payload = ''
    distant = 0
    pinMode(buzzer_pin, 'OUTPUT')
    pinMode(button, 'INPUT')

    def checkMovement(self):
        self.distant = ultrasonicRead(self.ultrasonic_ranger)
        if self.distant <= 10:
            data = {'team':{'id':13},'sensor':{'id':2, 'state':False, 'value': 'GEVAAR!!!'}}
            headers = {'Content-Type': 'application/json'}
            req = requests.post(self.linkAPI, data = json.dumps(data), headers = headers)
        else
            data = {'team':{'id':13},'sensor':{'id':2, 'state':False, 'value': 'GEVAAR!!!'}}
            headers = {'Content-Type': 'application/json'}
            req = requests.post(self.linkAPI, data = json.dumps(data), headers = headers)

    def buzzOff(self):
        digitalWrite(2, 0)
