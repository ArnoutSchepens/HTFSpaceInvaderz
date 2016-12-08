from Buzzer import *
#import HumidityTemperature

class Main:

    buzzer = Buzzer()
    #humTemp = HumidityTemperature()

    while True:
        try:

            buzzer.buzz
            #humTemp.getTempHum




        except KeyboardInterrupt:
            digitalWrite(buzzer_pin, 0)
        except (IOError, TypeError) as e:
            print "Error"
