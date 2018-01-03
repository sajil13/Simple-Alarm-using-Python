import time
import datetime
import win32api
str1 = input("What is the alarm for: ")
hr,minu = input("Set the time for the alarm in hh:mm format ").split(":")
t = datetime.datetime.now()
if t.second == 0:
    pass
else:
    time.sleep(60-t.second)
while True:
    
    now  = datetime.datetime.now()
    cr_hr = now.hour
    cr_min = now.minute
    
    if cr_hr == int(hr) and cr_min == int(minu):
        win32api.MessageBox(0,str1,"Alert",0x00001000)
        break
    time.sleep(60)
