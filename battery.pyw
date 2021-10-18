#copy change
import psutil,time
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("opened!!!",duration=10)
while(True):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    while(plugged==True):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        if percent=='100':
            toaster.show_toast("remove charger!!!",duration=10)
            break
        else:
            time.sleep(300)
    if percent<='10' and plugged==False:
        toaster.show_toast("plug battery immediately!!!!!",duration=10)
        time.sleep(100)
    elif percent<='25' and plugged==False:
        toaster.show_toast("battery low!!!",duration=10)
        time.sleep(300)
    else:
        time.sleep(300)
    
