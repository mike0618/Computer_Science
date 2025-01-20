import customtkinter as ctk
from PIL import Image, ImageTk


class MPG(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MPG Calculator")
        self.geometry("250x300")
        self.mode = ctk.StringVar()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        # ctk.set_window_scaling(2)
        ctk.set_widget_scaling(2)
        ctk.set_window_scaling(2)
        # set app icon
        img = Image.open("mpg.png")
        ctk_img = ImageTk.PhotoImage(img)
        self.wm_iconphoto(False, ctk_img)

        # Create widgets
        self.mode_switch = ctk.CTkSwitch(
            self,
            width=30,
            height=10,
            switch_width=30,
            switch_height=16,
            text="☼",
            variable=self.mode,
            command=self.set_mode,
            onvalue="light",
            offvalue="dark",
        )
        self.input_frame = ctk.CTkFrame(self)
        self.start_label = ctk.CTkLabel(self.input_frame, text="Start Mileage:")
        self.end_label = ctk.CTkLabel(self.input_frame, text="End Mileage:")
        self.gallons_label = ctk.CTkLabel(self.input_frame, text="Gallons Used:")
        self.start_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.end_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.gallons_entry = ctk.CTkEntry(self.input_frame, width=100)

        self.result_frame = ctk.CTkFrame(self)
        self.miles_label = ctk.CTkLabel(self.result_frame, text="Miles Driven:")
        self.mpg_label = ctk.CTkLabel(self.result_frame, text="MPG:")
        self.miles_entry = ctk.CTkEntry(self.result_frame, width=100, state="disabled")
        self.mpg_entry = ctk.CTkEntry(self.result_frame, width=100, state="disabled")
        self.calc_btn = ctk.CTkButton(
            self.result_frame, text="Calculate", width=100, command=self.calculate
        )

        # Show widgets
        self.mode_switch.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="e")
        self.input_frame.grid(row=1, column=0, padx=10, pady=10)
        self.start_label.grid(row=0, column=0, padx=10, sticky="e")
        self.end_label.grid(row=1, column=0, padx=10, sticky="e")
        self.gallons_label.grid(row=2, column=0, padx=10, sticky="e")
        self.start_entry.grid(row=0, column=1, padx=10, sticky="e", pady=10)
        self.end_entry.grid(row=1, column=1, padx=10, sticky="e")
        self.gallons_entry.grid(row=2, column=1, padx=10, sticky="e", pady=10)

        self.result_frame.grid(row=2, column=0, padx=10, pady=(0, 10))
        self.miles_label.grid(row=0, column=0, padx=10, sticky="e")
        self.mpg_label.grid(row=1, column=0, padx=10, sticky="e")
        self.miles_entry.grid(row=0, column=1, padx=10, sticky="e", pady=10)
        self.mpg_entry.grid(row=1, column=1, padx=10, sticky="e")
        self.calc_btn.grid(row=2, column=0, columnspan=2, sticky="we", padx=10, pady=10)
        self.input_frame.columnconfigure(0, minsize=220)
        self.result_frame.columnconfigure(0, minsize=220)

        self.start_entry.focus()
        self.bind("<Return>", lambda event: self.calculate())
        self.bind("<Escape>", lambda event: self.destroy())

    def set_mode(self):
        # it works in place
        ctk.set_appearance_mode(self.mode.get())

    def check_input(self, txt: str) -> float:
        # handeling user input
        if txt.replace(".", "", 1).isdigit():
            return float(txt)
        return 0.0

    def set_entry(self, entry, value):
        value = f"{value:.1f}".rstrip("0").strip(".")
        entry.configure(state="normal")
        entry.delete(0, "end")
        entry.insert(0, value)
        entry.configure(state="disabled")

    def calculate(self):
        start = self.start_entry.get().strip().replace(",", "")
        start = self.check_input(start)
        end = self.end_entry.get().strip().replace(",", "")
        end = self.check_input(end)
        gallons = self.gallons_entry.get().strip().replace(",", "")
        gallons = self.check_input(gallons)
        miles = end - start
        self.set_entry(self.miles_entry, miles)
        if gallons:  # to prevent zero-division
            mpg = miles / gallons
            self.set_entry(self.mpg_entry, mpg)


if __name__ == "__main__":
    app = MPG()
    app.mainloop()
