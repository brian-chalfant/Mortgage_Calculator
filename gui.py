from tkinter import *
from tkinter import messagebox
from mortgatecalc import mortgage

top = Tk()
frame = Frame(top, bd=6, height=55, width=65).pack()

home_cost = StringVar()
apr = StringVar()


def show_message(home_cost,apr):
    home_cost = int(home_cost.get())
    apr = float(apr.get())
    data = mortgage(home_cost, apr)
    messagebox.showinfo('Result', data)


finance_amount_entry_label = Label(frame, text="Financed Amount:", bg="Red").pack()
finance_amount_entry_textbox = Entry(frame, textvariable=home_cost).pack()
finance_amount_apr_label = Label(frame, text="APR Percentage", bg="Blue").pack()
finance_amount_apr_textbox = Entry(frame, textvariable=apr).pack()
finance_calculate_button = Button(frame, text="Submit", command=lambda: show_message(home_cost, apr), bg="Green").pack()
top.mainloop()
