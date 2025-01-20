import customtkinter as ctk
from converter import Temp_conv
from PIL import Image, ImageTk
from os.path import exists
import json


class TempConvGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Load settings
        if exists("settings.json"):
            with open("settings.json") as f:
                settings = json.load(f)
                self.mode = settings["mode"]
                self.theme = settings["theme"]
                self.precision = settings["precision"]
        else:
            self.mode = "dark"
            self.theme = "green"
            self.precision = 2

        self.title("Temperature Converter")
        # self.geometry("400x350")
        ctk.set_appearance_mode(self.mode)
        ctk.set_default_color_theme(self.theme)
        # ctk.set_window_scaling(2)
        ctk.set_widget_scaling(2)
        # set app icon
        img = Image.open("temp.png")
        ctk_img = ImageTk.PhotoImage(img)
        self.wm_iconphoto(False, ctk_img)
        # CircleCalculator instance
        self.converter = Temp_conv()

        # Create widgets
        self.main_frame = ctk.CTkFrame(self)
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.result_frame = ctk.CTkFrame(self.main_frame)
        self.settings_frame = ctk.CTkFrame(self)
        self.precision_frame = ctk.CTkFrame(self.settings_frame)
        self.appearance_frame = ctk.CTkFrame(self.settings_frame)
        self.settings_btn = ctk.CTkButton(
            self, text="Settings", width=100, command=self.show_settings
        )
        self.save_btn = ctk.CTkButton(self, text="Save", width=100, command=self.save)
        self.close_btn = ctk.CTkButton(
            self,
            text="Close",
            width=50,
            fg_color="pale violet red",
            hover_color="violet red",
            command=self.destroy,
        )
        self.cancel_btn = ctk.CTkButton(
            self,
            text="Cancel",
            width=50,
            fg_color="pale violet red",
            hover_color="violet red",
            command=self.show_main,
        )
        self.title_label = ctk.CTkLabel(
            self.main_frame, text="Enter Fahrenheit Temperature"
        )
        self.input_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.convert_btn = ctk.CTkButton(
            self.input_frame, text="Convert", width=100, command=self.convert
        )
        self.celsius_label = ctk.CTkLabel(self.result_frame, text="Celsius:")
        self.kelvin_label = ctk.CTkLabel(self.result_frame, text="Kelvin:")
        self.celsius_result = ctk.CTkLabel(self.result_frame, text="")
        self.kelvin_result = ctk.CTkLabel(self.result_frame, text="")
        self.settings_label = ctk.CTkLabel(self.settings_frame, text="Settings")
        self.precision_label = ctk.CTkLabel(self.precision_frame, text="Precision")
        self.precision_slider = ctk.CTkSlider(
            self.precision_frame,
            from_=0,
            to=9,
            number_of_steps=9,
            command=self.set_precision,
            width=180,
        )
        self.precision_slider.set(self.precision)
        self.precision_number = ctk.CTkLabel(
            self.precision_frame, text=f"{self.precision}"
        )
        self.appearance_label = ctk.CTkLabel(self.appearance_frame, text="Appearance")
        self.mode_label = ctk.CTkLabel(self.appearance_frame, text="Mode")
        self.theme_label = ctk.CTkLabel(self.appearance_frame, text="Theme")
        self.mode_menu = ctk.CTkOptionMenu(
            self.appearance_frame,
            values=["system", "dark", "light"],
            command=self.set_mode,
            width=100,
        )
        self.mode_menu.set(self.mode)
        self.theme_menu = ctk.CTkOptionMenu(
            self.appearance_frame,
            values=["blue", "dark-blue", "green"],
            command=self.set_theme,
            width=100,
        )
        self.theme_menu.set(self.theme)
        self.show_main()
        self.bind("<Return>", lambda event: self.convert())

    def set_precision(self, value):
        value = int(value)
        self.precision_number.configure(text=value)
        self.precision = value

    def set_mode(self, value):
        self.mode = value
        # it works in place
        ctk.set_appearance_mode(self.mode)

    def set_theme(self, value):
        # does not work in place, only after restart
        self.theme = value

    def convert(self):
        # handeling user input and negative numbers
        mult = 1
        f = self.input_entry.get().strip().replace(",", "")
        if f and f[0] == "-":
            f = f[1:]
            mult = -1
        if not f.replace(".", "", 1).isdigit():
            return 0
        f = float(f) * mult
        # make conversion and display results
        celsius = self.converter.ftoc(f)
        kelvin = self.converter.ftok(f)
        self.celsius_result.configure(text=f"{celsius:.{self.precision}f} °C")
        self.kelvin_result.configure(text=f"{kelvin:.{self.precision}f} °K")

    def show_main(self):
        self.save_btn.grid_remove()
        self.cancel_btn.grid_remove()
        self.settings_frame.grid_remove()
        # Window elements
        self.settings_btn.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.close_btn.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.main_frame.grid(row=1, column=0, columnspan=2, padx=10)
        # Main frame window elements
        self.title_label.grid(row=0, column=0, padx=10, sticky="w")
        self.input_frame.grid(row=1, column=0, padx=10, pady=(0, 10))
        self.result_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="we")
        # Input frame window elements
        self.input_entry.grid(row=0, column=0, padx=10, pady=10)
        self.convert_btn.grid(row=0, column=1, padx=10)
        # Result frame window elements
        self.celsius_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.celsius_result.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.kelvin_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
        self.kelvin_result.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="w")
        self.input_entry.focus()

    def show_settings(self):
        self.settings_btn.grid_remove()
        self.close_btn.grid_remove()
        self.main_frame.grid_remove()
        # Window elements
        self.save_btn.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.cancel_btn.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.settings_frame.grid(row=1, column=0, columnspan=2, padx=10)
        # Settings frame window elements
        self.settings_label.grid(row=0, column=0, padx=10, sticky="w")
        self.precision_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="we")
        self.appearance_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="we")
        # Precision frame window elements
        self.precision_label.grid(row=0, column=0, columnspan=2, padx=10)
        self.precision_slider.grid(row=1, column=0, padx=10)
        self.precision_number.grid(row=1, column=1, padx=10)
        # Appearance frame window elements
        self.appearance_label.grid(row=0, column=0, columnspan=2, padx=10)
        self.mode_label.grid(row=1, column=0, padx=10, sticky="we")
        self.mode_menu.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="we")
        self.theme_label.grid(row=1, column=1, padx=10, sticky="we")
        self.theme_menu.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="we")

    def save(self):
        data = {"precision": self.precision, "mode": self.mode, "theme": self.theme}
        self.convert()
        with open("settings.json", "w") as f:
            json.dump(data, f)
        self.show_main()


if __name__ == "__main__":
    app = TempConvGUI()
    app.mainloop()
