import pickle
import customtkinter as ctk
from os.path import exists


# TODO: Create a class for gui
class GUI:
    def __init__(self) -> None:
        # set db_file for pickle and variables
        self.DB_FILE = "pickle_file"
        self.team = self.read_db()
        # set appearance settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # create main window with paddings and title
        self.app = ctk.CTk()
        self.app.geometry("630x240")
        self.app.config(padx=15, pady=15)
        self.app.title("Team Roaster")

        # define gui elements
        self.name_entry = ctk.CTkComboBox(
            self.app, values=list(self.team.keys()), command=self.on_select
        )
        self.name_entry.grid(row=0, column=0, columnspan=2, sticky="new")
        self.pos_entry = ctk.CTkEntry(self.app)
        self.pos_entry.grid(row=1, column=0, columnspan=2, sticky="new")
        self.del_btn = ctk.CTkButton(
            self.app,
            text="Delete",
            fg_color="pale violet red",
            hover_color="violet red",
            command=self.delete,
        )
        self.del_btn.grid(padx=(0, 4), row=2, column=0, sticky="n")
        self.save_btn = ctk.CTkButton(self.app, text="Save", command=self.save)
        self.save_btn.grid(padx=(4, 0), row=2, column=1, sticky="n")
        self.team_scroll = ctk.CTkTextbox(
            self.app, width=300, height=186, font=("mono", 14)
        )
        self.team_scroll.grid(padx=(8, 0), row=0, rowspan=3, column=2, sticky="ew")
        self.info_lbl = ctk.CTkLabel(self.app, text="")
        self.info_lbl.grid(pady=4, row=3, column=0, columnspan=3, sticky="new")
        # initial set of interface
        self.update_gui()
        self.on_select(self.name_entry.get())
        # save or update using Enter
        self.app.bind("<Return>", lambda event: self.save())

    # TODO: Create functions to read/write the file using pickle
    def read_db(self):
        if not exists(self.DB_FILE):
            return {}
        with open(self.DB_FILE, "rb") as f:
            return pickle.load(f)

    def write_db(self):
        with open(self.DB_FILE, "wb") as f:
            pickle.dump(self.team, f)
        self.update_gui()

    # TODO: Create operational functions for buttons
    def save(self):
        # save/update a new entry and write db
        name = self.name_entry.get()
        if not name:
            return False
        pos = self.pos_entry.get()
        msg = f"Added {name} to the team as {pos}"
        if name in self.team:
            msg = f"Updated {name}'s position to {pos}"
        self.team[name] = pos
        self.info_lbl.configure(text=msg)
        self.write_db()

    def delete(self):
        # delete a name from dict, clean entries and save db
        name = self.name_entry.get()
        if not name:
            return False
        self.team.pop(name, None)
        self.name_entry.set("")
        self.pos_entry.delete(0, "end")
        self.info_lbl.configure(text=f"Removed {name} from the team")
        self.write_db()

    # TODO: Create helper functions
    def update_gui(self):
        # gui refresh function
        if not self.team:
            self.name_entry.set("")
        self.team_scroll.delete("1.0", "end")
        maxl = 0
        for n in self.team:  # to align the team list in the textbox by :
            if len(n) > maxl:
                maxl = len(n)
        for n, p in self.team.items():
            self.team_scroll.insert("end", " " * (maxl - len(n)) + f"{n}: {p}\n")
        self.name_entry.configure(values=list(self.team.keys()))
        self.name_entry.focus()

    def on_select(self, choice):
        # if a name selected from the combobox, set its position
        if choice:
            self.pos_entry.delete(0, "end")
            self.pos_entry.insert(0, self.team.get(choice))


if __name__ == "__main__":
    gui = GUI()
    gui.app.mainloop()
