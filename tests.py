import tkinter as tk

from backend.data import create_sample_courses
from backend.scheduler import Scheduler
from frontend.calendar_view import CalendarView


def test_scheduler():

    courses = create_sample_courses()

    scheduler = Scheduler(courses)

    result = scheduler.solve()

    assert result is not None

    sections = list(result.values())

    for i in range(len(sections)):
        for j in range(i + 1, len(sections)):
            assert not sections[i].conflicts_with(sections[j])


def test_calendar_view_schedule_display():

    root = tk.Tk()
    root.withdraw()

    try:
        view = CalendarView(root)
        view.clear_schedule()
        view.display_schedule(None)

        courses = create_sample_courses()
        scheduler = Scheduler(courses)
        view.display_schedule(scheduler.solve())
    finally:
        root.destroy()


if __name__ == "__main__":
    test_scheduler()
    test_calendar_view_schedule_display()
    print("Forward checking test passed.")