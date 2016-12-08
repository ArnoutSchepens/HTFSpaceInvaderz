import time
from grovepi import *
import math
import requests
import json
from grove_rgb_lcd import *

class buzz:

    buzzer_pin = 2
    button = 4
    previousInput = 0
    buttonPushed = False
    button_status = False
    buzzing = False
    linkAPI = 'http://192.168.50.148:4000/api'
    payload = ''
    pinMode(buzzer_pin, 'OUTPUT')
    pinMode(button, 'INPUT')

    def buzz(self):

        self.buttonPushed = self.button_status
        self.button_status = digitalRead(self.button)
        if(self.button_status == self.buttonPushed):
            print("niets")
        else:
            if(self.button_status and self.buzzing == False):
                digitalWrite(self.buzzer_pin, 1)
                self.buzzing = True
                data = {'team':{'id':13},'sensor':{'id':0, 'state':False, 'value': 'GEVAAR!!!'}}
                headers = {'Content-Type': 'application/json'}
                req = requests.post(linkAPI, data = json.dumps(data), headers = headers)
            elif(self.button_status and self.buzzing == True):
                digitalWrite(self.buzzer_pin, 0)
                self.buzzing = False
                headers = {'Content-Type': 'application/json'}
                data = {'team':{'id':13},'sensor':{'id':0, 'state':True, 'value': 'Alles Ok'}}
                req = requests.post(linkAPI, data = json.dumps(data), headers = headers)


    def buzzOff(self):
        digitalWrite(2, 0)
