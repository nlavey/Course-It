import tkinter as tk

from frontend.sidebar import Sidebar
from frontend.calendar_view import CalendarView


class SchedulerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Course Scheduler")

        self.geometry("1200x700")

        self.sidebar = Sidebar(
            self,
            self.generate_schedule,
        )

        self.sidebar.pack(
            side="left",
            fill="y",
        )

        self.calendar = CalendarView(self)

        self.calendar.pack(
            side="right",
            fill="both",
            expand=True,
        )

    def generate_schedule(self):

        selected = self.sidebar.get_selected_courses()

        print("Selected courses:")

        for course in selected:
            print(course)