# use Tkinter GUI to show a digital clock
from Tkinter import *
import time
root = Tk()
time1 = ''
clock = Label(root, font=('times', 80, 'bold'), bg='YELLOW')
clock.pack(fill=BOTH, expand=2)
def tick():
    global time1
    #time format
    #time taken from device
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    # updating every seconds
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
root.mainloop(  )