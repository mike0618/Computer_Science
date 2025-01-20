import customtkinter as ctk
from circle import CircleCalculator


class CircleCalculatorGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Circe's Circle/Sector Calculator")
        self.geometry("400x350")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.columnconfigure(3, minsize=120)

        # CircleCalculator instance
        self.calc = CircleCalculator()

        # Create widgets
        self.create_widgets()
        self.bind("<Return>", lambda event: self.calculate())
        self.entry_radius.focus()

    def calculate(self):
        radius_input = self.entry_radius.get()
        angle_input = self.entry_angle.get()
        if not radius_input:
            return False
        selected_units = self.unit_choice.get()[0].lower()
        if not angle_input:
            angle_input = "360"
            selected_units = "d"

        # Set radius, angle units and angle
        self.calc.set_radius(radius_input)
        self.calc.set_units(selected_units)
        self.calc.set_angle(angle_input)

        # Display results
        self.entry_diam.configure(text=f"{self.calc.calc_diameter():,.2f}")
        self.entry_area.configure(text=f"{self.calc.calc_area():,.2f}")
        self.entry_ark.configure(text=f"{self.calc.calc_ark():,.2f}")
        self.entry_radius.focus()

    def create_widgets(self):
        # Radius input
        self.label_radius = ctk.CTkLabel(self, text="Enter radius:")
        self.label_radius.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_radius = ctk.CTkEntry(self)
        self.entry_radius.grid(row=0, column=1, padx=10, pady=10)

        # Angle input
        self.label_angle = ctk.CTkLabel(self, text="Enter angle:")
        self.label_angle.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_angle = ctk.CTkEntry(self)
        self.entry_angle.grid(row=1, column=1, padx=10, pady=10)

        # Angle unit combobox
        self.label_units = ctk.CTkLabel(self, text="Select angle units:")
        self.label_units.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.unit_choice = ctk.StringVar(value="d")
        self.combobox_units = ctk.CTkComboBox(
            self,
            values=["Degrees (d)", "Radians (r)", "Pi (p)"],
            variable=self.unit_choice,
        )
        self.combobox_units.grid(row=2, column=1, padx=10, pady=10)

        # Diameter input
        self.label_diam = ctk.CTkLabel(self, text="Diameter:")
        self.label_diam.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.entry_diam = ctk.CTkLabel(self, text="")
        self.entry_diam.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        # Area input
        self.label_area = ctk.CTkLabel(self, text="Area:")
        self.label_area.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.entry_area = ctk.CTkLabel(self, text="")
        self.entry_area.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        # Ark input
        self.label_ark = ctk.CTkLabel(self, text="Ark length:")
        self.label_ark.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        self.entry_ark = ctk.CTkLabel(self, text="")
        self.entry_ark.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        # Calculate button
        self.button_calc = ctk.CTkButton(self, text="Calculate", command=self.calculate)
        self.button_calc.grid(
            row=3, column=2, columnspan=2, padx=10, pady=10, sticky="we"
        )


if __name__ == "__main__":
    app = CircleCalculatorGUI()
    app.mainloop()
