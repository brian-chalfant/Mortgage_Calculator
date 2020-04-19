from tkinter import *
from tkinter import messagebox
from mortgatecalc import mortgage


class Mortgage_Calc:
    def __init__(self):
        self.top = Tk()
        self.frame = Frame(self.top).pack()
        self.home_cost = StringVar()
        self.apr = StringVar()
        self.build_gui()

    def show_message(self):
        home_cost_int = int(self.home_cost.get())
        apr_float = float(self.apr.get())
        data = mortgage(home_cost_int, apr_float)
        messagebox.showinfo('Result', data)

    def build_gui(self):
        finance_amount_entry_label = Label(self.frame, text="Financed Amount:", bg="White", font=("Times New Roman", 14)).pack()
        finance_amount_entry_textbox = Entry(self.frame, textvariable=self.home_cost).pack()
        finance_amount_apr_label = Label(self.frame, text="APR Percentage", bg="White").pack()
        finance_amount_apr_textbox = Entry(self.frame, textvariable=self.apr).pack()
        finance_calculate_button = Button(self.frame, text="Submit", command=lambda: self.show_message(), bg="White").pack()
        self.top.mainloop()


if __name__ == '__main__':
    newinstance = Mortgage_Calc()
