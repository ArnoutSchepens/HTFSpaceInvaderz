from grove_rgb_lcd import *
from grovepi import *

class HumidityTemperature:

    dhtSensorPort = 7

    def getTempHum(self):
        [ tmp,hum ] = dht(dhtSensorPort, 1)

        print "Temp =", temp, "C\thumidity =", hum, "%"
        t = str(temp)
        h = str(hum)

        print("Temp: " + t + "C\tHumidity =" + h + "%")
        setRGB(0,128,64)
        setRGB(0,255,0)
        setText("Temp: " + t + "C\tHumidity =" + h + "%")
