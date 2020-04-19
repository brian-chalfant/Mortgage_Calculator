import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from mortgatecalc import mortgage


class Mortgage_Calc:
    def __init__(self):
        self.top = tk.Tk()
        self.top.title("Mortgage Calculator")
        self.stile = ttk.Style()
        self.stile.configure('My.TFrame', padding=10, relief='flat')
        self.stile.configure('My.Label', padding=5, anchor='center', relief='Sunken', background='#00ffcc',
                             font=('Impact', 15), align='c', width=15)
        self.stile.configure("TButton", padding=6, relief="flat", background="#00ffcc")
        self.frame = ttk.Frame(self.top, style='My.TFrame').grid()
        self.home_cost = tk.StringVar()
        self.apr = tk.StringVar()

        self.build_gui()



    def show_message(self):
        home_cost_int = int(self.home_cost.get())
        apr_float = float(self.apr.get())
        data = mortgage(home_cost_int, apr_float)
        messagebox.showinfo('Result', data)

    def build_gui(self):
        finance_amount_entry_label = ttk.Label(self.frame, text="Financed Amount: ", style='My.Label', width=25).grid(row=0, column=0)
        finance_amount_entry_textbox = ttk.Entry(self.frame, textvariable=self.home_cost).grid(row=0, column=1)
        finance_amount_apr_label = ttk.Label(self.frame, text="APR Percentage: ", style='My.Label', width=25).grid(row=1, column=0)
        finance_amount_apr_textbox = ttk.Entry(self.frame, textvariable=self.apr).grid(row=1, column=1)
        finance_calculate_button = ttk.Button(self.frame, text="Calculate", style='TButton',
                                              command=lambda: self.show_message()).grid(row=2, columnspan=2, sticky=tk.E+tk.W)
        self.top.mainloop()


if __name__ == '__main__':
    newinstance = Mortgage_Calc()
