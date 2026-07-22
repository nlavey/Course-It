from course import Course
from section import Section
from meeting_time import MeetingTime

cs101 = Course("CS101", "Intro to Programming")

cs101.add_section(
    Section(
        "CS101",
        "A",
        MeetingTime("MWF", "09:00", "09:50"),
        "Dr. Smith"
    )
)

cs101.add_section(
    Section(
        "CS101",
        "B",
        MeetingTime("TR", "11:00", "12:15"),
        "Dr. Jones"
    )
)

math201 = Course("MATH201", "Calculus I")

math201.add_section(
    Section(
        "MATH201",
        "A",
        MeetingTime("MWF", "09:30", "10:20"),
        "Dr. Brown"
    )
)

math201.add_section(
    Section(
        "MATH201",
        "B",
        MeetingTime("TR", "09:30", "10:45"),
        "Dr. Green"
    )
)

courses = [cs101, math201]