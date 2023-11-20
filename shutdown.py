import os
import time
from tkinter import *

def shutdown_at_time(hour, minute):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            os.system("shutdown now")
            break
        time.sleep(60)

def get_closing_time():
    global closing_hour_entry
    global closing_minute_entry

    closing_hour = int(closing_hour_entry.get())
    closing_minute = int(closing_minute_entry.get())

    shutdown_at_time(closing_hour, closing_minute)

root = Tk()
root.title("Shutdown Timer")

closing_hour_label = Label(root, text="Closing Hour:")
closing_hour_label.grid(row=0, column=0)

closing_hour_entry = Entry(root, width=2)
closing_hour_entry.grid(row=0, column=1)

closing_minute_label = Label(root, text="Closing Minute:")
closing_minute_label.grid(row=1, column=0)

closing_minute_entry = Entry(root, width=2)
closing_minute_entry.grid(row=1, column=1)

shutdown_button = Button(root, text="Shutdown", command=get_closing_time)
shutdown_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
