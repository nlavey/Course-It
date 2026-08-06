import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

from backend.data import get_available_courses, load_catalog_from_path
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
        self.search_var = tk.StringVar()
        self.selected_courses_state = set()

        search_label = tk.Label(self, text="Search courses")
        search_label.pack(anchor="w", padx=10, pady=(0, 2))

        self.search_entry = tk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack(fill="x", padx=10, pady=(0, 8))
        self.search_var.trace_add("write", lambda *_: self.refresh_course_list())

        self.course_frame = tk.Frame(self)
        self.course_frame.pack(fill="both", expand=True)
        self.refresh_course_list()

        import_button = tk.Button(
            self,
            text="Import Course Catalog (.csv)",
            command=self.import_catalog,
        )
        import_button.pack(fill="x", padx=10, pady=(10, 5))

        self.status_var = tk.StringVar(value="Using built-in catalog")
        self.status_label = tk.Label(
            self,
            textvariable=self.status_var,
            wraplength=220,
            justify="left",
            fg="#444444",
        )
        self.status_label.pack(fill="x", padx=10, pady=(0, 10))

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

    def refresh_course_list(self):
        for widget in self.course_frame.winfo_children():
            widget.destroy()

        self.variables = {}
        selected_courses = set(self.get_selected_courses())

        search_text = (self.search_var.get() or "").strip().lower()

        for course in get_available_courses():
            course_code = course.course_code
            course_name = course.course_name or ""
            if search_text and search_text not in course_code.lower() and search_text not in course_name.lower():
                continue

            var = tk.BooleanVar(value=course_code in selected_courses)

            check = tk.Checkbutton(
                self.course_frame,
                text=course_code,
                variable=var,
                anchor="w",
            )

            check.pack(fill="x", padx=15, pady=2)

            self.variables[course_code] = var

    def import_catalog(self):
        file_path = filedialog.askopenfilename(
            title="Select a course catalog CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )

        if not file_path:
            return

        try:
            courses = load_catalog_from_path(file_path)
        except FileNotFoundError:
            messagebox.showerror("Import failed", f"Unable to find file:\n{file_path}")
            return
        except ValueError as exc:
            messagebox.showerror("Import failed", str(exc))
            return

        self.refresh_course_list()
        self.status_var.set(f"Loaded {len(courses)} courses from {Path(file_path).name}")

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