import tkinter as tk

from backend.data import get_course_names
from backend.preferences import Preference


class Sidebar(tk.Frame):

    def __init__(self, parent, generate_callback):
        super().__init__(parent, width=260)

        self.pack_propagate(False)

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

        preference_title = tk.Label(
            self,
            text="Scheduling Preference",
            font=("Arial", 12, "bold"),
        )
        preference_title.pack(pady=(10, 5))

        self.preference_var = tk.StringVar(value=Preference.FEWEST_GAPS)
        self.preference_frame = tk.Frame(self)
        self.preference_frame.pack(fill="x", padx=(15, 10))

        for preference in Preference.ALL:
            radio = tk.Radiobutton(
                self.preference_frame,
                text=Preference.LABELS[preference],
                variable=self.preference_var,
                value=preference,
                anchor="w",
            )
            radio.pack(fill="x", pady=1, anchor="w")

        generate_button = tk.Button(
            self,
            text="Generate Schedule",
            command=self.generate_schedule,
        )

        generate_button.pack(fill="x", padx=10, pady=10)

    def select_preference(self, preference):
        self.preference_var.set(preference)

    def get_selected_courses(self):
        selected = []

        for name, variable in self.variables.items():
            if variable.get():
                selected.append(name)

        return selected

    def get_selected_preference(self):
        return self.preference_var.get()

    def generate_schedule(self):
        selected = self.get_selected_courses()
        preference = self.get_selected_preference()

        self.generate_callback(selected, preference)