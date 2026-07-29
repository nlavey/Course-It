import tkinter as tk

from backend.data import get_course_names


class Sidebar(tk.Frame):

    def __init__(self, parent, generate_callback):
        super().__init__(parent, width=260)

        self.pack_propagate(False)

        # Save callback
        self.generate_callback = generate_callback

        title = tk.Label(
            self,
            text="Course Selection",
            font=("Arial", 14, "bold"),
        )
        title.pack(pady=(15, 10))

        self.variables = {}

        self.course_frame = tk.Frame(self)
        self.course_frame.pack(fill="both", expand=True)

        for name in get_course_names():

            var = tk.BooleanVar()

            check = tk.Checkbutton(
                self.course_frame,
                text=name,
                variable=var,
                anchor="w",
            )

            check.pack(fill="x", padx=15, pady=2)

            self.variables[name] = var

        generate_button = tk.Button(
            self,
            text="Generate Schedule",
            command=self.generate_schedule,
        )

        generate_button.pack(fill="x", padx=10, pady=10)

    def get_selected_courses(self):

        selected = []

        for name, variable in self.variables.items():

            if variable.get():
                selected.append(name)

        return selected

    def generate_schedule(self):

        selected = self.get_selected_courses()

        self.generate_callback(selected)