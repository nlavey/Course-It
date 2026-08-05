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


def _format_time(minutes):
    hour = minutes // 60
    minute = minutes % 60
    suffix = "AM" if hour < 12 else "PM"
    if hour > 12:
        hour -= 12
    if hour == 0:
        hour = 12
    return f"{hour}:{minute:02d} {suffix}"


def _build_block_text(section):
    course_code = getattr(section, "course_code", None) or getattr(getattr(section, "course", None), "code", None)
    section_id = getattr(section, "section_id", None)
    instructor = getattr(section, "instructor", "")
    room = getattr(section, "room", None) or getattr(getattr(section, "meeting_time", None), "room", None)

    parts = [course_code]
    if section_id:
        parts.append(f"Section {section_id}")
    if room:
        parts.append(f"Room {room}")
    if instructor:
        parts.append(instructor)

    meeting_times = getattr(section, "meeting_times", None)
    if meeting_times is None:
        meeting_time = getattr(section, "meeting_time", None)
        meeting_times = [meeting_time] if meeting_time is not None else []
    elif not isinstance(meeting_times, list):
        meeting_times = [meeting_times]

    detail_lines = []
    for meeting_time in meeting_times:
        if meeting_time is None:
            continue

        days = meeting_time.days if isinstance(meeting_time.days, list) else [meeting_time.day]
        for day in days:
            detail_lines.append(
                f"{day}: {_format_time(meeting_time.start)}-{_format_time(meeting_time.end)}"
            )

    if detail_lines:
        parts.extend(detail_lines)

    return "\n".join(parts)


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
    color_index = 0

    for section in sections:

        if isinstance(section, dict):
            section = section.get("section") or section.get("selected_section")

        course_code = getattr(section, "course_code", None)
        if course_code is None and getattr(section, "course", None) is not None:
            course_code = getattr(section.course, "code", None)

        if course_code is None:
            continue

        if course_code not in color_map:
            color_map[course_code] = COLORS[color_index % len(COLORS)]
            color_index += 1

        color = color_map[course_code]

        meeting_times = getattr(section, "meeting_times", None)
        if meeting_times is None:
            meeting_time = getattr(section, "meeting_time", None)
            meeting_times = [meeting_time] if meeting_time is not None else []
        elif not isinstance(meeting_times, list):
            meeting_times = [meeting_times]

        instructor = getattr(section, "instructor", "")
        block_text = _build_block_text(section)

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
                text=block_text,
                bg=color,
                relief="raised",
                bd=1,
                justify="center",
                wraplength=140,
                font=("Segoe UI", 8)
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