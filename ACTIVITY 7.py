from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import calendar

root = tk.Tk()
root.geometry("1920x1080")
root.title('Calendar')


def show():
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y, m)

    cal.insert('end', output)


def clear():
    cal.delete(1.0, "end")


def exit_():
    root.destroy()


img = ImageTk.PhotoImage(Image.open("calendar64x64.png"))
label = Label(image=img)
label.place(x=170, y=0)

m_label = Label(root, text="Month", font=('verdana', '10', 'bold'))
m_label.place(x=120, y=80)

month = Spinbox(root, from_=11, to=12, width=5)
month.place(x=180, y=80)

y_label = Label(root, text="Year", font=('veranda', '10', 'bold'))
y_label.place(x=210, y=80)

year = Spinbox(root, from_=2023, to=3000, width=8)
year.place(x=260, y=80)

cal = Text(root, width=33, height=8, relief=RIDGE, borderwidth=2)
cal.place(x=90, y=250)

show = Button(root, text="Show", font=('verdana', '10', 'bold'), relief=RIDGE, borderwidth=2, command=show)
show.place(x=140, y=200)

clear = Button(root, text="Clear", font=('verdana', '10', 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear.place(x=200, y=200)

exit__ = Button(root, text="Exit", font=('verdana', '10', 'bold'), relief=RIDGE, borderwidth=2, command=exit_)
exit__.place(x=260, y=200)

root.mainloop()
