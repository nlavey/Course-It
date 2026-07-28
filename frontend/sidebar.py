import tkinter as tk

from frontend.colors import *


class Sidebar(tk.Frame):

    def __init__(self, parent):

        super().__init__(
            parent,
            bg=SIDEBAR,
            width=250
        )

        self.pack_propagate(False)

        title = tk.Label(
            self,
            text="Course Scheduler",
            bg=SIDEBAR,
            fg=TEXT_LIGHT,
            font=("Arial", 18, "bold")
        )

        title.pack(pady=20)