import tkinter as tk
from threading import Thread, Event
from time import localtime, sleep


class ThreadingApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Threading with Tkinter")
        self.setup_gui()
        self.stop_event = Event()
        # handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def setup_gui(self):
        self.lbl_disp = tk.Label(self.root, text="Threading with Tkinter")
        self.lbl_disp.grid(row=0, column=0, columnspan=2, pady=20)
        start_btn = tk.Button(self.root, text="Start Thread", command=self.start_thread)
        start_btn.grid(row=1, column=0, pady=20, padx=10)
        stop_btn = tk.Button(self.root, text="Stop Thread", command=self.stop_thread)
        stop_btn.grid(row=1, column=1, pady=20, padx=10)

    def bg_task(self):
        while not self.stop_event.is_set():
            now = localtime()
            now = f"{now.tm_hour:02d}:{now.tm_min:02d}:{now.tm_sec:02d}"
            self.lbl_disp.config(text=f"Running background task {now}")
            sleep(1)

    def start_thread(self):
        self.stop_event.clear()
        self.thread = Thread(target=self.bg_task, daemon=True)
        # daemon=True stops when program ends
        self.thread.start()

    def stop_thread(self):
        self.stop_event.set()
        self.lbl_disp.config(text="Background task stopped")

    def on_closing(self):
        self.stop_thread()
        self.root.destroy()


if __name__ == "__main__":
    app = ThreadingApp()
