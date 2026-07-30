import tkinter as tk

from .colors import *


class CalendarView(tk.Frame):

    def __init__(self, master):
        super().__init__(
            master,
            bg=CALENDAR_BG
        )

        self.build_ui()

    def build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = tk.Label(
            self,
            text="Weekly Schedule",
            bg=CALENDAR_BG,
            font=TITLE_FONT
        )

        title.pack(
            pady=20
        )

        # -------------------------
        # Calendar Grid
        # -------------------------

        self.grid_frame = tk.Frame(
            self,
            bg=CALENDAR_BG
        )

        self.message_label = tk.Label(
            self,
            text="",
            bg=CALENDAR_BG,
            font=("Segoe UI", 11),
            fg="#4C566A"
        )
        self.message_label.pack(pady=(0, 10))

        self.grid_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        days = [
            "",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ]

        time_slots = list(range(8 * 60, 18 * 60, 30))

        # Day headers
        for col, day in enumerate(days):
            label = tk.Label(
                self.grid_frame,
                text=day,
                bg=CALENDAR_BG,
                font=HEADER_FONT,
                relief="ridge",
                borderwidth=1,
                padx=8,
                pady=8
            )
            label.grid(row=0, column=col, sticky="nsew")

        # Time labels and empty cells
        for row, minutes in enumerate(time_slots, start=1):
            if minutes % 60 == 0:
                label_text = f"{minutes // 60}:00"
            else:
                label_text = f"{minutes // 60}:{minutes % 60:02d}"

            time_label = tk.Label(
                self.grid_frame,
                text=label_text,
                bg=CALENDAR_BG,
                font=NORMAL_FONT,
                relief="ridge",
                borderwidth=1,
                width=8
            )

            time_label.grid(row=row, column=0, sticky="nsew")

            for col in range(1, 6):
                cell = tk.Frame(
                    self.grid_frame,
                    bg="white",
                    relief="ridge",
                    borderwidth=1,
                    height=28
                )

                cell.grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )

        # Make rows and columns expand with the window
        for col in range(6):
            self.grid_frame.grid_columnconfigure(col, weight=1)

        for row in range(len(time_slots) + 1):
            self.grid_frame.grid_rowconfigure(row, weight=1)

    def clear_schedule(self):

        for widget in self.grid_frame.winfo_children():

            if getattr(widget, "is_course_block", False):
                widget.destroy()

    def display_schedule(self, schedule):

        self.clear_schedule()

        if schedule is None or schedule == []:
            self.message_label.config(text="No valid schedule exists yet. Try selecting different courses.")
            return

        self.message_label.config(text="")

        from frontend.renderer import draw_schedule

        draw_schedule(
            self.grid_frame,
            schedule
        )