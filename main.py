import tkinter as tk
from tkinter import font
import time


# create the main app class
class SirisWordPoofApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Siris Word Poof App")
        self.root.configure(bg="#f5f5dc")  # off-white/beige background

        # heading labels
        self.title_label = tk.Label(root, text="Siris Word Poof App", font=("Helvetica", 24), bg="#f5f5dc")
        self.title_label.pack(pady=10)

        self.subtitle_label = tk.Label(root, text="Don’t stop writing, or all progress will be lost.",
                                       font=("Helvetica", 14), bg="#f5f5dc")
        self.subtitle_label.pack(pady=5)

        # Text box for user to write
        self.text_area = tk.Text(root, wrap='word', height=10, font=("Helvetica", 14))
        self.text_area.pack(padx=20, pady=10)

        # "Start Writing" button
        self.start_button = tk.Button(root, text="Start Writing", font=("Helvetica", 14), fg="red", bg="white",
                                      activeforeground="red", activebackground="white", command=self.start_writing,
                                      relief="groove", borderwidth=2)
        self.start_button.pack(pady=10)

        # create a custom font that we can adjust for the fuzzy effect
        self.custom_font = font.Font(self.text_area, self.text_area.cget("font"))
        self.text_area.configure(font=self.custom_font)

        # timers and tracking variables
        self.last_typed_time = None
        self.typing_fuzz_timer = None
        self.typing_reset_timer = None
        self.is_typing = False

        # bind text area to detect typing
        self.text_area.bind('<KeyPress>', self.on_key_press)

    def on_key_press(self, event):
        self.is_typing = True
        self.last_typed_time = time.time()

        # reset text back to normal if user starts typing again
        self.custom_font.config(weight="normal", slant="roman")
        self.text_area.configure(fg="black")

        # cancel any timers if user types
        if self.typing_fuzz_timer:
            self.root.after_cancel(self.typing_fuzz_timer)
        if self.typing_reset_timer:
            self.root.after_cancel(self.typing_reset_timer)

        # set new timers
        self.typing_fuzz_timer = self.root.after(5000, self.make_text_fuzzy)  # 5 seconds to go fuzzy
        self.typing_reset_timer = self.root.after(5000, self.clear_text)  # 5 seconds to delete text

    def make_text_fuzzy(self):
        # make the text fuzzy by changing its weight and color
        self.custom_font.config(weight="bold", slant="italic")
        self.text_area.configure(fg="grey")

    def clear_text(self):
        # if user stops typing for 5 seconds, clear the text area
        self.text_area.delete('1.0', tk.END)

    def start_writing(self):
        # reset all settings when the user clicks "Start Writing"
        self.text_area.delete('1.0', tk.END)
        self.custom_font.config(weight="normal", slant="roman")
        self.text_area.configure(fg="black")
        self.last_typed_time = None


# create tkinter window
root = tk.Tk()

# set the geometry of the window
root.geometry("600x400")

# create app instance
app = SirisWordPoofApp(root)

# run the main loop
root.mainloop()
