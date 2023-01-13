''' Python Mortgage Calculator - Programmer: Simge Yildirimkaya '''
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

# Create window
root = Tk()
root.title('Calculate Your Mortgage')
root.geometry("700x500")


def payment():
  if amount_entry.get() and interest_entry.get() and term_entry.get(
  ) and downPay_entry.get():
    
    years = float(term_entry.get())
    months = years * 12
    rate = float(interest_entry.get())
    loan = float(amount_entry.get())
    dpp = float(downPay_entry.get())

    # ---Monthly Payment Calculation---

    # Down Payment
    dpp = dpp / 100
    dp = dpp * loan
    amt = loan - dp
    # Monthly Interest Rate
    monthly_rate = (rate / 100) / 12
    # Payment Equation
    payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * amt
    # Format the payment
    payment = f"{payment:,.2f}"
    # Output Payment to the screen
    payment_label.config(text=f"Monthly Payment: ${payment}")

  else:
    payment_label.config(text="Fill Out All Boxes.")


# Create GUI
my_label_frame = LabelFrame(root, text="Mortgage Calculator")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Define Label and Entry Boxes
amount_label = Label(my_frame, text="Loan Amount")
amount_entry = Entry(my_frame, font=("Times", 24))

interest_label = Label(my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("Times", 24))

term_label = Label(my_frame, text="Term (years)")
term_entry = Entry(my_frame, font=("Times", 24))

downPay_label = Label(my_frame, text="Down Payment %")
downPay_entry = Entry(my_frame, font=("Times", 24))

# Placement of Label and Entry Boxes
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20)

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

downPay_label.grid(row=3, column=0, padx=20)
downPay_entry.grid(row=3, column=1, pady=20)

# Button
my_button = Button(my_label_frame, text="Calculate Payment", command=payment)
my_button.pack(pady=20)

# Output Label
payment_label = Label(root, text="", font=("Times", 24))
payment_label.pack(pady=20)

#Styles
style = ttk.Style()
root.configure(bg="pink")
style.configure("TEntry", foreground="purple")

root.mainloop()
