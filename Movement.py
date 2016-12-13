import time
from grovepi import *
import math
import requests
import json
from grove_rgb_lcd import *

class movement:

    ultrasonic_ranger = 3
    linkAPI = 'http://192.168.50.148:4000/api'
    distant = 0

    def checkMovement(self):
        self.distant = ultrasonicRead(self.ultrasonic_ranger)
        if self.distant <= 10:
            data = {'team':{'id':13},'sensor':{'id':2, 'state':False, 'value': 'GEVAAR!!!'}}
            headers = {'Content-Type': 'application/json'}
            req = requests.post(self.linkAPI, data = json.dumps(data), headers = headers)
        else:
            data = {'team':{'id':13},'sensor':{'id':2, 'state':False, 'value': 'Alles Ok!!!'}}
            headers = {'Content-Type': 'application/json'}
            req = requests.post(self.linkAPI, data = json.dumps(data), headers = headers)
