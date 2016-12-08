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
    payload = '';
    pinMode(buzzer_pin, 'OUTPUT')
    pinMode(button, 'INPUT')

    def buzz(self):
        buttonPushed = button_status
        button_status = digitalRead(button)
        if(button_status == buttonPushed):
            print("niets")
        else:
            if(button_status and buzzing == False):
                digitalWrite(buzzer_pin, 1)
                buzzing = True
                #payload = {'team':{'id':13},'sensor':[{'id':0},{'state':True}, {'value', 'WARNING!!!'}]}
            elif(button_status and buzzing == True):
                digitalWrite(buzzer_pin, 0)
                buzzing = False
                #payload = {'team':{'id':13},'sensor':[{'id':0},{'state':False}, {'value', 'Alles ok!'}]}
                #Als JSON
        #r = request.post(linkAPI, data=payload)
