import csv
from pathlib import Path

from backend.course import Course
from backend.section import Section
from backend.meeting_time import MeetingTime

DATA_DIR = Path(__file__).parent.parent / "data"
REQUIRED_COLUMNS = ["Course", "Title", "Section", "Days", "Start", "End"]


def load_catalog(filename):
    """
    Load a course catalog from a CSV file and return a list of Course objects.
    """

    csv_path = _resolve_catalog_path(filename)
    courses = {}
    section_map = {}

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty.")

        missing_columns = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]
        if missing_columns:
            raise ValueError(f"Missing required column: {missing_columns[0]}")

        for row_number, row in enumerate(reader, start=2):
            code = (row.get("Course") or "").strip()
            if not code:
                raise ValueError(f"Row {row_number} is missing a course code.")

            title = (row.get("Title") or "").strip()
            section_id = (row.get("Section") or "").strip()
            days = (row.get("Days") or "").strip()

            if code not in courses:
                courses[code] = Course(code, title)

            section_key = (code, section_id)
            section = section_map.get(section_key)

            start_time = (row.get("Start") or "").strip()
            end_time = (row.get("End") or "").strip()

            try:
                meeting_times = [
                    MeetingTime(day, start_time, end_time)
                    for day in _split_days(days)
                ]
            except ValueError as exc:
                raise ValueError(
                    f"Unable to parse meeting time: {start_time}-{end_time}"
                ) from exc

            if section is None:
                section = Section(
                    code,
                    section_id,
                    meeting_times,
                    (row.get("Instructor") or "").strip(),
                )
                section_map[section_key] = section
                courses[code].add_section(section)
            else:
                section.meeting_times.extend(meeting_times)

    return list(courses.values())


def _resolve_catalog_path(filename):
    path = Path(filename)
    if path.is_absolute():
        return path

    candidate = DATA_DIR / path
    if candidate.exists():
        return candidate

    return candidate


def _split_days(days_string):
    if not days_string:
        return []

    days_string = days_string.strip()
    if "," in days_string or " " in days_string:
        tokens = [token.strip() for token in days_string.replace(",", " ").split() if token.strip()]
        return tokens

    tokens = []
    index = 0
    while index < len(days_string):
        if days_string.startswith("Th", index):
            tokens.append("Th")
            index += 2
        elif days_string.startswith("Tu", index):
            tokens.append("Tu")
            index += 2
        else:
            tokens.append(days_string[index])
            index += 1

    return tokens
