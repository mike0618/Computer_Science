from polyangle import Polyangle
import customtkinter as ctk
# from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.pl = Polyangle()
        self.title("PolyAngle")
        self.geometry("250x450")
        self.mode = ctk.StringVar()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        # ctk.set_window_scaling(2)
        ctk.set_widget_scaling(2)
        ctk.set_window_scaling(2)
        # set app icon
        # img = Image.open("icon.png")
        # ctk_img = ImageTk.PhotoImage(img)
        # self.wm_iconphoto(False, ctk_img)

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
        self.sides_lbl = ctk.CTkLabel(self.input_frame, text="N Sides:")
        self.len_lbl = ctk.CTkLabel(self.input_frame, text="Length of Side:")
        self.sides_ent = ctk.CTkEntry(self.input_frame, width=100)
        self.len_ent = ctk.CTkEntry(self.input_frame, width=100)

        self.result_frame = ctk.CTkFrame(self)
        self.name_lbl = ctk.CTkLabel(self.result_frame, text="Name:")
        self.name_ent = ctk.CTkEntry(self.result_frame, width=100, state="disabled")
        self.int_angle_lbl = ctk.CTkLabel(self.result_frame, text="Interior Angle:")
        self.int_angle_ent = ctk.CTkEntry(
            self.result_frame, width=100, state="disabled"
        )
        self.ext_angle_lbl = ctk.CTkLabel(self.result_frame, text="Exterior Angle:")
        self.ext_angle_ent = ctk.CTkEntry(
            self.result_frame, width=100, state="disabled"
        )
        self.perimeter_lbl = ctk.CTkLabel(self.result_frame, text="Perimeter:")
        self.perimeter_ent = ctk.CTkEntry(
            self.result_frame, width=100, state="disabled"
        )
        self.inrad_lbl = ctk.CTkLabel(self.result_frame, text="Inradius:")
        self.inrad_ent = ctk.CTkEntry(self.result_frame, width=100, state="disabled")
        self.crad_lbl = ctk.CTkLabel(self.result_frame, text="Circumradius:")
        self.crad_ent = ctk.CTkEntry(self.result_frame, width=100, state="disabled")
        self.area_lbl = ctk.CTkLabel(self.result_frame, text="Area:")
        self.area_ent = ctk.CTkEntry(self.result_frame, width=100, state="disabled")

        self.calc_btn = ctk.CTkButton(
            self.result_frame, text="Calculate", width=100, command=self.calculate
        )

        # Show widgets
        self.mode_switch.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="e")
        self.input_frame.grid(row=1, column=0, padx=10, pady=10)
        self.sides_lbl.grid(row=0, column=0, padx=10, sticky="e")
        self.sides_ent.grid(row=0, column=1, padx=10, sticky="e", pady=10)
        self.len_lbl.grid(row=1, column=0, padx=10, sticky="e", pady=(0, 10))
        self.len_ent.grid(row=1, column=1, padx=10, sticky="e", pady=(0, 10))

        self.result_frame.grid(row=2, column=0, padx=10, pady=(0, 10))
        self.name_lbl.grid(row=0, column=0, padx=10, sticky="e")
        self.name_ent.grid(row=0, column=1, padx=10, sticky="e", pady=10)
        self.int_angle_lbl.grid(row=1, column=0, padx=10, sticky="e", pady=(0, 10))
        self.int_angle_ent.grid(row=1, column=1, padx=10, sticky="e", pady=(0, 10))
        self.ext_angle_lbl.grid(row=2, column=0, padx=10, sticky="e", pady=(0, 10))
        self.ext_angle_ent.grid(row=2, column=1, padx=10, sticky="e", pady=(0, 10))
        self.perimeter_lbl.grid(row=3, column=0, padx=10, sticky="e", pady=(0, 10))
        self.perimeter_ent.grid(row=3, column=1, padx=10, sticky="e", pady=(0, 10))
        self.inrad_lbl.grid(row=4, column=0, padx=10, sticky="e", pady=(0, 10))
        self.inrad_ent.grid(row=4, column=1, padx=10, sticky="e", pady=(0, 10))
        self.crad_lbl.grid(row=5, column=0, padx=10, sticky="e", pady=(0, 10))
        self.crad_ent.grid(row=5, column=1, padx=10, sticky="e", pady=(0, 10))
        self.area_lbl.grid(row=6, column=0, padx=10, sticky="e", pady=(0, 10))
        self.area_ent.grid(row=6, column=1, padx=10, sticky="e", pady=(0, 10))

        self.calc_btn.grid(
            row=7, column=0, columnspan=2, sticky="we", padx=10, pady=(0, 10)
        )
        self.input_frame.columnconfigure(0, minsize=220)
        self.result_frame.columnconfigure(0, minsize=220)

        self.sides_ent.focus()
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

    def set_ent(self, entry, value, num=True, deg=False):
        if num:
            value = f"{value:.2f}".rstrip("0").strip(".")
            if deg:
                value += "°"
        entry.configure(state="normal")
        entry.delete(0, "end")
        entry.insert(0, value)
        entry.configure(state="disabled")

    def calculate(self):
        sides = self.sides_ent.get().strip().replace(",", "")
        sides = self.check_input(sides)
        length = self.len_ent.get().strip().replace(",", "")
        length = self.check_input(length)
        self.pl.sides(sides)
        self.pl.side_len(length)
        self.set_ent(self.name_ent, self.pl.name(), num=False)
        self.set_ent(self.int_angle_ent, self.pl.interior(), deg=True)
        self.set_ent(self.ext_angle_ent, self.pl.exterior(), deg=True)
        self.set_ent(self.perimeter_ent, self.pl.perimeter())
        self.set_ent(self.inrad_ent, self.pl.inradius())
        self.set_ent(self.crad_ent, self.pl.circumradius())
        self.set_ent(self.area_ent, self.pl.area())


if __name__ == "__main__":
    app = App()
    app.mainloop()
