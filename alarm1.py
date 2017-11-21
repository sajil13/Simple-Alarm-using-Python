import time
import datetime

from tkinter import *

from tkinter import messagebox
hr,minu = input("Set the time for the alarm in hh:mm format").split(":")

while True:
    
    now  = datetime.datetime.now()
    cr_hr = now.hour
    cr_min = now.minute
    
    if cr_hr == int(hr) and cr_min == int(minu):
        messagebox.showinfo("Alert","Times Up Buddy!! Get Up")
    time.sleep(3600)
