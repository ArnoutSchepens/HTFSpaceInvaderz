from Buzzer import buzz
from  HumidityTemperature import *

class Main:

    buzzer = buzz()
    #humTemp = HumidityTemperature()

    while True:
        try:

            buzzer.buzz()
            #humTemp.getTempHum




        except KeyboardInterrupt:
            digitalWrite(buzzer_pin, 0)
        except (IOError, TypeError) as e:
            print(e)
