import tkinter as tk

from frontend.colors import *


class CalendarView(tk.Frame):

    def __init__(self, parent):

        super().__init__(
            parent,
            bg=CONTENT
        )

        label = tk.Label(
            self,
            text="Weekly Schedule",
            font=("Arial", 18, "bold"),
            bg=CONTENT
        )

        label.pack(pady=20)