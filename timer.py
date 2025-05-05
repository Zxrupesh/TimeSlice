import tkinter as tk
from playsound import playsound
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch / Countdown Timer")
        self.root.geometry("400x400")  # Set window size
        self.root.configure(bg="#2E2E2E")  # Background color

        # Time variables
        self.time_left = 0
        self.is_running = False

        # Timer label
        self.label = tk.Label(root, text="00:00", font=("Helvetica", 40, "bold"), fg="white", bg="#2E2E2E")
        self.label.pack(pady=30)

        # Time input components
        self.time_entry_label = tk.Label(root, text="Set Time (mm:ss)", font=("Helvetica", 12), fg="white", bg="#2E2E2E")
        self.time_entry_label.pack()

        self.time_entry = tk.Entry(root, font=("Helvetica", 14), width=10)
        self.time_entry.pack(pady=10)

        self.set_button = tk.Button(root, text="Set Time", width=15, height=2, font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.set_time)
        self.set_button.pack(pady=10)

        # Control buttons with modern look
        self.button_frame = tk.Frame(root, bg="#2E2E2E")
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", width=10, height=2, font=("Helvetica", 12), bg="#2196F3", fg="white", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = tk.Button(self.button_frame, text="Pause", width=10, height=2, font=("Helvetica", 12), bg="#FFC107", fg="white", command=self.pause_timer)
        self.pause_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", width=10, height=2, font=("Helvetica", 12), bg="#F44336", fg="white", command=self.reset_timer)
        self.reset_button.pack(side="left", padx=10)

    def set_time(self):
        try:
            minutes, seconds = map(int, self.time_entry.get().split(":"))
            self.time_left = minutes * 60 + seconds
            self.update_label()
        except ValueError:
            self.label.config(text="Invalid input")

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def pause_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.time_left = 0
        self.update_label()

    def countdown(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_label()
            self.root.after(1000, self.countdown)
        elif self.time_left == 0 and self.is_running:
            playsound("alert.mp3")  # Play sound when timer ends

    def update_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

