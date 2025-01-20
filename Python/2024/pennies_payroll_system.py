import customtkinter as ctk  # pip install customtkinter  # GUI library

# set appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# create main window with paddings and title
app = ctk.CTk()
app.config(padx=15, pady=15)
app.title("Penny's Payroll System")

# TODO: Create constants
OVERTIME_PAY = 40
OVERTIME_RATE = 1.5
BONUS_A = 0.1
BONUS_B = 0.05


# TODO: Get and check user input
def get_input(obj):
    user_input = obj.get().strip().replace(",", "")
    if user_input.replace(".", "", 1).isdigit():
        return float(user_input)
    return False


# TODO: Show results function
def show(name, reg, over, bonus, gross):
    namepay_res_lbl.configure(text=name)
    regpay_res_lbl.configure(text=f"$ {reg:,.2f}")
    overtime_res_lbl.configure(text=f"$ {over:,.2f}")
    bonuspay_res_lbl.configure(text=f"$ {bonus:,.2f}")
    gross_res_lbl.configure(text=f"$ {gross:,.2f}")


def calculate():
    """
    calculate payroll
    """
    # TODO: save user input in variables
    name = name_entry.get().strip()
    hours = get_input(hours_entry)
    rate = get_input(rate_entry)
    bonus_input = bonus_entry.get().strip()
    if not all((name, hours, rate)):
        show("", 0, 0, 0, 0)
        return False
    # TODO: calculate payroll
    overhours = 0
    if hours > OVERTIME_PAY:
        overhours = hours - OVERTIME_PAY
        hours = OVERTIME_PAY
    regpay = hours * rate
    overpay = overhours * rate * OVERTIME_RATE
    bonus_rate = 0
    if bonus_input.upper() == "A":
        bonus_rate = BONUS_A
    elif bonus_input.upper() == "B":
        bonus_rate = BONUS_B
    bonus = (regpay + overpay) * bonus_rate
    gross = regpay + overpay + bonus
    # TODO: Show results
    show(name, regpay, overpay, bonus, gross)


# set necessary GUI elements: entries, button and lables
name_lbl = ctk.CTkLabel(app, text="Enter Name: ")
name_lbl.grid(row=0, column=0, sticky="W")
hours_lbl = ctk.CTkLabel(app, text="Enter Hours: ")
hours_lbl.grid(row=1, column=0, sticky="W")
rate_lbl = ctk.CTkLabel(app, text="Enter Rate: ")
rate_lbl.grid(row=2, column=0, sticky="W")
bonuscode_lbl = ctk.CTkLabel(app, text="Enter Bonus Code (A, B): ")
bonuscode_lbl.grid(row=3, column=0, sticky="W")
name_entry = ctk.CTkEntry(app, placeholder_text="Name")
name_entry.grid(row=0, column=1)
hours_entry = ctk.CTkEntry(app, placeholder_text="Hours")
hours_entry.grid(row=1, column=1)
rate_entry = ctk.CTkEntry(app, placeholder_text="Rate")
rate_entry.grid(row=2, column=1)
bonus_entry = ctk.CTkEntry(app, placeholder_text="Bonus Code")
bonus_entry.grid(row=3, column=1)
conv_btn = ctk.CTkButton(app, text="Calculate", command=calculate)
conv_btn.grid(row=4, column=0, columnspan=2, sticky="WE", pady=15)
namepay_lbl = ctk.CTkLabel(app, text="Payroll Advise: ")
namepay_lbl.grid(row=5, column=0, sticky="W")
regpay_lbl = ctk.CTkLabel(app, text="Regular Pay: ")
regpay_lbl.grid(row=6, column=0, sticky="W")
overtime_lbl = ctk.CTkLabel(app, text="Overtime Pay: ")
overtime_lbl.grid(row=7, column=0, sticky="W")
bonuspay_lbl = ctk.CTkLabel(app, text="Bonus: ")
bonuspay_lbl.grid(row=8, column=0, sticky="W")
gross_lbl = ctk.CTkLabel(app, text="Gross Pay: ")
gross_lbl.grid(row=9, column=0, sticky="W")
namepay_res_lbl = ctk.CTkLabel(app, text="")
namepay_res_lbl.grid(row=5, column=1, sticky="W")
regpay_res_lbl = ctk.CTkLabel(app, text="")
regpay_res_lbl.grid(row=6, column=1, sticky="W")
overtime_res_lbl = ctk.CTkLabel(app, text="")
overtime_res_lbl.grid(row=7, column=1, sticky="W")
bonuspay_res_lbl = ctk.CTkLabel(app, text="")
bonuspay_res_lbl.grid(row=8, column=1, sticky="W")
gross_res_lbl = ctk.CTkLabel(app, text="")
gross_res_lbl.grid(row=9, column=1, sticky="W")
name_entry.focus()

# to calculate by hitting Enter
app.bind("<Return>", lambda event: calculate())

app.mainloop()
