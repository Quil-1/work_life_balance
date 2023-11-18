import tkinter as tk
from tkinter import messagebox

def set_alarm():
    if hour and minute and am_pm:
        time_12h = f"{hour}:{minute} {am_pm}"
        messagebox.showinfo("Work and Life", f"Closing Hour Set for {time_12h}")
    else:
        messagebox.showwarning("Work and Life", "Please select hour, minute, and AM/PM.")

def on_hour_select(event=None):
    global hour
    #get the hour value from the dropdown
    hour = hour_dropdown.get(hour_dropdown.curselection()[0]) if hour_dropdown.curselection() else ""

def on_minute_select(event=None):
    global minute
    #get the minute value from the dropdown
    minute = minute_dropdown.get(minute_dropdown.curselection()[0]) if minute_dropdown.curselection() else ""

def on_am_pm_select(event=None):
    global am_pm
    #get the AM/PM value from the dropdown
    am_pm = am_pm_dropdown.get(am_pm_dropdown.curselection()[0]) if am_pm_dropdown.curselection() else ""

def print_current_values():
    print(f"Hour: {hour}, Minute: {minute}, AM/PM: {am_pm}")

def create_gui():
    root = tk.Tk()
    root.title("Work and Life")
    root.geometry("300x250")
    root.configure(bg="#75d701")

    selection_frame = tk.Frame(root, padx=10, pady=10, bg="#75d701")
    selection_frame.pack(expand=True)

    hour_label = tk.Label(selection_frame, text="Hour:", font=("Arial", 12), bg="#75d701", fg="white")
    hour_label.grid(row=0, column=0, padx=5, pady=5)
    hour_options = [str(i) for i in range(1, 13)]
    global hour_dropdown
    hour_dropdown = tk.Listbox(selection_frame, exportselection=False, font=("Arial", 12), height=1, width=3)
    hour_dropdown.grid(row=0, column=1, padx=5, pady=5)
    for i in hour_options:
        hour_dropdown.insert("end", i)
    hour_dropdown.bind("<<ListboxSelect>>", on_hour_select)

    minute_label = tk.Label(selection_frame, text="Minute:", font=("Arial", 12), bg="#75d701", fg="white")
    minute_label.grid(row=1, column=0, padx=5, pady=5)
    minute_options = [f"{i:02d}" for i in range(0, 60)]
    global minute_dropdown
    minute_dropdown = tk.Listbox(selection_frame, exportselection=False, font=("Arial", 12), height=1, width=3)
    minute_dropdown.grid(row=1, column=1, padx=5, pady=5)
    for i in minute_options:
        minute_dropdown.insert("end", i)
    minute_dropdown.bind("<<ListboxSelect>>", on_minute_select)

    am_pm_label = tk.Label(selection_frame, text="AM/PM:", font=("Arial", 12), bg="#75d701", fg="white")
    am_pm_label.grid(row=2, column=0, padx=5, pady=5)
    am_pm_options = ["AM", "PM"]
    global am_pm_dropdown
    am_pm_dropdown = tk.Listbox(selection_frame, exportselection=False, font=("Arial", 12), height=1, width=3)
    am_pm_dropdown.grid(row=2, column=1, padx=5, pady=5)
    for i in am_pm_options:
        am_pm_dropdown.insert("end", i)
    am_pm_dropdown.bind("<<ListboxSelect>>", on_am_pm_select)

    set_alarm_button = tk.Button(selection_frame, text="Set Work Closing Hour", font=("Arial", 12), command=set_alarm)
    set_alarm_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    print_values_button = tk.Button(selection_frame, text="Print Current Values", font=("Arial", 12), command=print_current_values)
    print_values_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
