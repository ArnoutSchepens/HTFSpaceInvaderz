from Buzzer import *
from  HumidityTemperature import *

class Main:

    buzzer = Buzzer()
    #humTemp = HumidityTemperature()

    while True:
        try:

            Buzzer.buzz()
            #humTemp.getTempHum




        except KeyboardInterrupt:
            digitalWrite(buzzer_pin, 0)
        except (IOError, TypeError) as e:
            print "Error"
