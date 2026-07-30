import tkinter as tk

from frontend.sidebar import Sidebar
from frontend.calendar_view import CalendarView

from backend.scheduler import Scheduler
from backend.data import get_courses_by_codes

from .navigator import Navigator


class SchedulerApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Course Scheduler")
        self.geometry("1200x750")
        self.schedules = []
        self.current_schedule = 0

        self.sidebar = Sidebar(
            self,
            self.generate_schedule
        )

        self.content_frame = tk.Frame(self, bg="white")
        self.calendar = CalendarView(self.content_frame)

        self.navigator = Navigator(
            self.content_frame,
            self.previous_schedule,
            self.next_schedule
        )

        self.sidebar.pack(side="left", fill="y")
        self.content_frame.pack(side="right", fill="both", expand=True)
        self.calendar.pack(side="top", fill="both", expand=True)
        self.navigator.pack(side="bottom", fill="x", pady=(0, 10))
        self.navigator.update(0, 0)

    def generate_schedule(self, selected_courses, preference=None):

        self.current_schedule = 0

        if not selected_courses:
            self.schedules = []
            self.calendar.display_schedule(None)
            self.navigator.update(self.current_schedule, len(self.schedules))
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
        scheduler = Scheduler(chosen_courses, preference=preference)
        schedules = scheduler.solve()
        self.schedules = list(schedules)

        if self.schedules:
            self.calendar.display_schedule(self.schedules[self.current_schedule])
        else:
            self.calendar.display_schedule([])

        self.navigator.update(self.current_schedule, len(self.schedules))

    def previous_schedule(self):

        if not self.schedules:
            return

        if self.current_schedule > 0:
            self.current_schedule -= 1
            self.calendar.display_schedule(self.schedules[self.current_schedule])
            self.navigator.update(self.current_schedule, len(self.schedules))

    def next_schedule(self):

        if not self.schedules:
            return

        if self.current_schedule < len(self.schedules) - 1:
            self.current_schedule += 1
            self.calendar.display_schedule(self.schedules[self.current_schedule])
            self.navigator.update(self.current_schedule, len(self.schedules))