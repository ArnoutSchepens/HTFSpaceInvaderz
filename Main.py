import Buzzer

class main:

    buzzer = Buzzer()

    while True:
        try:

            Buzzer.buzz()



        except KeyboardInterrupt:
            digitalWrite(buzzer_pin, 0)
        except (IOError, TypeError) as e:
            print "Error"
