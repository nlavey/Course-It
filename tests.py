import tkinter as tk

import pytest

from backend.data import create_sample_courses
from backend.data_loader import load_catalog
from backend.preferences import Preference
from backend.scheduler import Scheduler
from frontend.calendar_view import CalendarView
from frontend.navigator import Navigator
from frontend.sidebar import Sidebar


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


def test_navigator_empty_state():

    root = tk.Tk()
    root.withdraw()

    try:
        navigator = Navigator(root, lambda: None, lambda: None)
        navigator.update(0, 0)

        assert navigator.label.cget("text") == "0 of 0"
        assert navigator.previous_button.cget("state") == "disabled"
        assert navigator.next_button.cget("state") == "disabled"
    finally:
        root.destroy()


def test_calendar_view_message_for_empty_schedule():

    try:
        root = tk.Tk()
    except tk.TclError as exc:
        pytest.skip(f"Tk is not available in this environment: {exc}")

    root.withdraw()

    try:
        view = CalendarView(root)
        view.display_schedule([])

        assert view.message_label is not None
        assert "No valid schedule" in view.message_label.cget("text")
    finally:
        root.destroy()


def test_sidebar_preference_selection_uses_callback():

    try:
        root = tk.Tk()
    except tk.TclError as exc:
        pytest.skip(f"Tk is not available in this environment: {exc}")

    root.withdraw()

    try:
        calls = []

        def callback(selected_courses, preference):
            calls.append((selected_courses, preference))

        sidebar = Sidebar(root, callback)
        sidebar.select_preference(Preference.NO_FRIDAY)

        sidebar.generate_schedule()

        assert calls[0][1] == Preference.NO_FRIDAY
    finally:
        root.destroy()


def test_sidebar_live_search_filters_courses():
    try:
        root = tk.Tk()
    except tk.TclError as exc:
        pytest.skip(f"Tk is not available in this environment: {exc}")

    root.withdraw()

    try:
        sidebar = Sidebar(root, lambda *_: None)
        sidebar.search_var.set("CSE")
        sidebar.refresh_course_list()

        assert "CSE101" in sidebar.variables
        assert "MATH19A" not in sidebar.variables
    finally:
        root.destroy()


def test_load_catalog_reports_missing_required_columns(tmp_path):
    catalog_path = tmp_path / "catalog.csv"
    catalog_path.write_text(
        "Course,Title,Section,Days,End\n"
        "CS101,Intro,01,MW,10:00\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required column: Start"):
        load_catalog(catalog_path)


def test_load_catalog_reports_invalid_meeting_time(tmp_path):
    catalog_path = tmp_path / "catalog.csv"
    catalog_path.write_text(
        "Course,Title,Section,Days,Start,End\n"
        "CS101,Intro,01,MW,9am-10:15,10:15\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Unable to parse meeting time"):
        load_catalog(catalog_path)


if __name__ == "__main__":
    test_scheduler()
    test_calendar_view_schedule_display()
    print("Forward checking test passed.")