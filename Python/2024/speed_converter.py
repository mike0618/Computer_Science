import customtkinter as ctk  # pip install customtkinter  # GUI library

# set appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# create main window with paddings and title
app = ctk.CTk()
app.config(padx=15, pady=15)
app.title("Speed Converter")

# useful dictionary with measures and conversion factors
conversion_dict = {
    "Miles per Hour": 1,
    "Kilometer per Hour": 1.60934,
    "Barleycorns per Day": 24 * 189334.58824,
    "Furlongs per Fortnight": 2687.99,
    "Mach Number": 1 / 767.269,
    "% Speed Light": 100 / 670616629,
    "Days to reach the Moon": 10000,
    "Knots (Nautical MPH)": 0.868976,  # 1 / 1.15078
    "Meters per Second": 1609.34 / 3600,
}
val_lbls = []


def convert():
    """
    Convert mph to different speed measures.
    """
    # some user input handling here
    mph = mph_entry.get().strip().replace(",", "")
    # clear the entry and focus on it
    mph_entry.delete(0, ctk.END)
    mph_entry.focus()
    if not mph or not mph.replace(".", "", 1).isdigit():
        return False
    mph = float(mph)
    # go through the conv dict
    for n, (measure, coef) in enumerate(conversion_dict.items()):
        fmt = ",.3f"  # default formatting
        if "Light" in measure or "Mach" in measure:
            fmt = ",.15f"  # precise formatting for these two measures
        if measure.startswith("Days") and mph:
            v = coef / mph  # special case, days to the moon is not speed
        else:
            v = mph * coef
        # show calculated measures in the GUI
        txt = f"{v:{fmt}}"
        val_lbls[n].configure(text=txt)


# set necessary GUI elements: entry, button and lables
mph_entry = ctk.CTkEntry(app, placeholder_text="Enter Speed in mph")
mph_entry.grid(row=0, column=0)
conv_btn = ctk.CTkButton(app, text="Convert MPH", command=convert)
conv_btn.grid(row=0, column=1, pady=15, padx=15)
for n, measure in enumerate(conversion_dict.keys()):
    measure_lbl = ctk.CTkLabel(app, text=measure + ": ")
    measure_lbl.grid(row=n + 1, column=0, sticky="E")
    value_lbl = ctk.CTkLabel(app, text="")
    value_lbl.grid(row=n + 1, column=1, sticky="W", padx=15)
    val_lbls.append(value_lbl)
mph_entry.focus()

# to convert by hitting Enter
app.bind("<Return>", lambda event: convert())

app.mainloop()
