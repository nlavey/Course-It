import tkinter as tk

from .sidebar import Sidebar
from .calendar_view import CalendarView
from .colors import *


class CourseSchedulerApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Course Scheduler")

        self.root.geometry("1200x700")

        self.root.configure(bg=WINDOW_BG)

        self.build_ui()

    def build_ui(self):

        sidebar = Sidebar(self.root)
        sidebar.pack(side="left", fill="y")

        calendar = CalendarView(self.root)
        calendar.pack(side="right", fill="both", expand=True)

    def run(self):
        self.root.mainloop()