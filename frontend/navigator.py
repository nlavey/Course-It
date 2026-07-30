import tkinter as tk


class Navigator(tk.Frame):

    def __init__(self, parent, previous_callback, next_callback):
        super().__init__(parent)

        self.previous_button = tk.Button(
            self,
            text="◀ Previous",
            command=previous_callback,
            width=12
        )

        self.previous_button.pack(side="left", padx=5)

        self.label = tk.Label(
            self,
            text="0 of 0",
            width=12
        )

        self.label.pack(side="left", padx=10)

        self.next_button = tk.Button(
            self,
            text="Next ▶",
            command=next_callback,
            width=12
        )

        self.next_button.pack(side="left", padx=5)

    def update(self, index, total):

        if total <= 0:
            self.label.config(text="0 of 0")
            self.previous_button.config(state="disabled")
            self.next_button.config(state="disabled")
            return

        display_index = min(index, total - 1)
        self.label.config(text=f"{display_index + 1} of {total}")

        self.previous_button.config(
            state=("normal" if display_index > 0 else "disabled")
        )

        self.next_button.config(
            state=("normal" if display_index < total - 1 else "disabled")
        )