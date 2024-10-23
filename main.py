from umar import Wifi 
from umar import Wifi2

device = Wifi("starlink 1000", "wert234rt45", "WPA3-Personal", "2.4GHz band", "$1000", "20th March")
print(device.description())
print(device.launch())
device = Wifi2("starlink 2000", "qwertghnjk", "WPA2/WPA3-Personal", "5/2.4GHz band", "$2500", "20th March" )
print(device.description1())
print(device.launch1())