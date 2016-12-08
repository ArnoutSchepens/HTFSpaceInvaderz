import time
from grovepi import *
import math
import requests
import json

buzzer_pin = 2
button = 4
previousInput = 0
buttonPushed = False
button_status = False
buzzing = False
linkAPI = 'http://192.168.50.148:4000/api'
payload = '';
print(r.text)
pinMode(buzzer_pin, 'OUTPUT')
pinMode(button, 'INPUT')
while True:
    try:
        buttonPushed = button_status
        button_status = digitalRead(button)
        if(button_status == buttonPushed):
            print("niets")
        else:
            if(button_status and buzzing == False):
                digitalWrite(buzzer_pin, 1)
                buzzing = True
                payload = {'team':{'id':13},'sensor':[{'id':0},{'state':True}, {'value', 'WARNING!!!'}]}
            elif(button_status and buzzing == True):
                digitalWrite(buzzer_pin, 0)
                buzzing = False
                payload = {'team':{'id':13},'sensor':[{'id':0},{'state':False}, {'value', 'Alles ok!'}]}

        r = request.post(linkAPI, data=payload)


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
