from Buzzer import buzz
from HumidityTemperature import *
from Movement import movement

class Main:

    buz = buzz()
    mov = movement()
    while True:
        try:
            #buz.buzz()
            #humTemp.getTempHum()
            mov.checkMovement()

        except KeyboardInterrupt:
            digitalWrite(2, 0)
        except (IOError, TypeError) as e:
            print(e)
