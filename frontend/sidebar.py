import tkinter as tk

from .colors import *


class Sidebar(tk.Frame):

    def __init__(self, master):
        super().__init__(
            master,
            bg=SIDEBAR_BG,
            width=260
        )

        self.pack_propagate(False)

        self.build_ui()

    def build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = tk.Label(
            self,
            text="Course Scheduler",
            bg=SIDEBAR_BG,
            font=TITLE_FONT
        )

        title.pack(
            pady=(20, 15)
        )

        # -------------------------
        # Section Header
        # -------------------------

        header = tk.Label(
            self,
            text="Course Selection",
            bg=SIDEBAR_BG,
            anchor="w",
            font=HEADER_FONT
        )

        header.pack(
            fill="x",
            padx=15,
            pady=(0, 8)
        )

        # -------------------------
        # Scrollable Frame
        # -------------------------

        container = tk.Frame(
            self,
            bg=SIDEBAR_BG
        )

        container.pack(
            fill="both",
            expand=True,
            padx=15
        )

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(
            container,
            bg="white",
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        scroll_frame = tk.Frame(
            canvas,
            bg="white"
        )

        frame_id = canvas.create_window(
            (0, 0),
            window=scroll_frame,
            anchor="nw"
        )

        def update_scrollregion(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def resize_frame(event):
            canvas.itemconfigure(frame_id, width=event.width)

        scroll_frame.bind("<Configure>", update_scrollregion)
        canvas.bind("<Configure>", resize_frame)

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        # -------------------------
        # Example Courses
        # -------------------------

        sample_courses = [
            "CSE 20",
            "CSE 30",
            "CSE 12",
            "CSE 13S",
            "CSE 16",
            "MATH 19A",
            "MATH 19B",
            "AM 10",
            "STAT 5",
            "PHYS 5A",
            "PHYS 5B",
            "ECON 1",
            "WRIT 1",
            "WRIT 2",
            "CSE 80N",
            "CSE 101",
            "CSE 120",
            "CSE 130",
            "CSE 183"
        ]

        self.course_vars = {}

        for course in sample_courses:

            var = tk.BooleanVar()

            chk = tk.Checkbutton(
                scroll_frame,
                text=course,
                variable=var,
                bg="white",
                anchor="w",
                font=NORMAL_FONT
            )

            chk.pack(
                fill="x",
                padx=8,
                pady=2
            )

            self.course_vars[course] = var

        # -------------------------
        # Generate Button
        # -------------------------

        button = tk.Button(
            self,
            text="Generate Schedule",
            bg=BUTTON_BG,
            fg=BUTTON_FG,
            font=HEADER_FONT,
            height=2
        )

        button.pack(
            fill="x",
            padx=15,
            pady=15
        )