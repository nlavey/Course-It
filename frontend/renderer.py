import tkinter as tk
import random


DAY_COLUMN = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5
}


COLORS = [
    "#8ecae6",
    "#219ebc",
    "#ffb703",
    "#fb8500",
    "#90be6d",
    "#f28482",
    "#cdb4db"
]


def minutes_to_row(minutes):

    return (minutes - 480) // 30 + 1


def draw_schedule(parent, schedule):

    if schedule is None:
        return

    if isinstance(schedule, dict):
        sections = list(schedule.values())
    elif isinstance(schedule, (list, tuple)):
        if schedule and isinstance(schedule[0], dict):
            sections = list(schedule[0].values())
        else:
            sections = list(schedule)
    else:
        sections = [schedule]

    color_map = {}

    for section in sections:

        if isinstance(section, dict):
            section = section.get("section") or section.get("selected_section")

        course_code = getattr(section, "course_code", None)
        if course_code is None and getattr(section, "course", None) is not None:
            course_code = getattr(section.course, "code", None)

        if course_code is None:
            continue

        if course_code not in color_map:
            color_map[course_code] = random.choice(COLORS)

        color = color_map[course_code]

        meeting_times = getattr(section, "meeting_times", None)
        if meeting_times is None:
            meeting_time = getattr(section, "meeting_time", None)
            meeting_times = [meeting_time] if meeting_time is not None else []
        elif not isinstance(meeting_times, list):
            meeting_times = [meeting_times]

        instructor = getattr(section, "instructor", "")

        for meeting_time in meeting_times:
            if meeting_time is None:
                continue

            row = minutes_to_row(meeting_time.start)

            span = max(
                1,
                (meeting_time.end - meeting_time.start) // 30
            )

            label = tk.Label(
                parent,
                text=f"{course_code}\n{instructor}",
                bg=color,
                relief="raised",
                bd=1,
                justify="center"
            )

            label.is_course_block = True

            label.grid(
                row=row,
                column=DAY_COLUMN[meeting_time.day],
                rowspan=span,
                sticky="nsew",
                padx=1,
                pady=1
            )