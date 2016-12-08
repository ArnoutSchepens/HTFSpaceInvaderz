import Buzzer

class main:

    buzzer = Buzzer()
    humTemp = HumidtyTemperature()

    while True:
        try:

            buzzer.buzz
            humTemp.getTempHum




        except KeyboardInterrupt:
            digitalWrite(buzzer_pin, 0)
        except (IOError, TypeError) as e:
            print "Error"
