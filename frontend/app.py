import tkinter as tk

from frontend.sidebar import Sidebar
from frontend.calendar_view import CalendarView

from backend.scheduler import Scheduler
from backend.data import get_courses_by_codes


class SchedulerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Course Scheduler")
        self.geometry("1200x750")

        self.sidebar = Sidebar(
            self,
            self.generate_schedule
        )

        self.calendar = CalendarView(self)

        self.sidebar.pack(side="left", fill="y")
        self.calendar.pack(side="right",
                           fill="both",
                           expand=True)

    def generate_schedule(self, selected_courses):

        if not selected_courses:
            self.calendar.display_schedule(None)
            return

        # Load all available courses
        all_courses = get_courses_by_codes(selected_courses)

        # Keep only the selected courses
        chosen_courses = [
            course
            for course in all_courses
            if course.course_code in selected_courses
        ]

        # Run the CSP solver
        scheduler = Scheduler(chosen_courses)
        schedule = scheduler.solve()

        # Display the result
        self.calendar.display_schedule(schedule)