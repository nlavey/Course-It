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

        calendar = tk.Frame(
            self,
            bg=CALENDAR_BG
        )

        calendar.pack(
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

        hours = list(range(8, 18))  # 8 AM to 5 PM

        # Day headers
        for col, day in enumerate(days):
            label = tk.Label(
                calendar,
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
        for row, hour in enumerate(hours, start=1):

            time_label = tk.Label(
                calendar,
                text=f"{hour}:00",
                bg=CALENDAR_BG,
                font=NORMAL_FONT,
                relief="ridge",
                borderwidth=1,
                width=8
            )

            time_label.grid(row=row, column=0, sticky="nsew")

            for col in range(1, 6):
                cell = tk.Frame(
                    calendar,
                    bg="white",
                    relief="ridge",
                    borderwidth=1,
                    height=50
                )

                cell.grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )

        # Make rows and columns expand with the window
        for col in range(6):
            calendar.grid_columnconfigure(col, weight=1)

        for row in range(len(hours) + 1):
            calendar.grid_rowconfigure(row, weight=1)