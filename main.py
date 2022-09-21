from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime
from datetime import datetime
import math

known_new = datetime(year=2000, month=1, day=6, hour=12, minute=24, second=1)
lunar_cycle = 29.53

def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    date2 = datetime.strptime(date, '%b %d, %Y')
    newdate = date2.replace(hour=datetime.now().hour, minute=datetime.now().minute, second=datetime.now().second)
    print(newdate)
    days = (newdate - known_new)
    totalmoons = days.days / 29.53
    print(totalmoons)
    f, t = math.modf(totalmoons)
    print(f)
    days_passed = f * lunar_cycle
    days_left = lunar_cycle - days_passed
    print(f'Faltam {days_left} dias para a proxima Lua Nova.')


    showinfo(message='{} was a {}'.format(date, weekday))

root = Tk()
label = Label(root, text='Digite uma data:')
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Click', command=clicked)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()


# New Moon = Every 29.53 days
# pm 1/6/2000 at 12:24:01, the moon was New.

# find the moon phase finding how many cycles has passed since a known new moon

# 1. find the number of days since a known new moon
# 2. dividing the number of days by the lunar period (29.53)
#