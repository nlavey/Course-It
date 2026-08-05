import csv
from pathlib import Path

from backend.course import Course
from backend.section import Section
from backend.meeting_time import MeetingTime

DATA_DIR = Path(__file__).parent.parent / "data"


def load_catalog(filename):
    """
    Load a course catalog from a CSV file and return a list of Course objects.
    """

    courses = {}
    section_map = {}

    csv_path = DATA_DIR / filename

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:

            code = row["Course"]

            if code not in courses:
                courses[code] = Course(
                    code,
                    row["Title"]
                )

            section_key = (code, row["Section"])
            section = section_map.get(section_key)

            meeting_times = [
                MeetingTime(day, row["Start"], row["End"])
                for day in _split_days(row["Days"])
            ]

            if section is None:
                section = Section(
                    code,
                    row["Section"],
                    meeting_times,
                    row.get("Instructor", "")
                )
                section_map[section_key] = section
                courses[code].add_section(section)
            else:
                section.meeting_times.extend(meeting_times)

    return list(courses.values())


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
