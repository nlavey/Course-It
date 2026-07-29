from backend.course import Course
from backend.section import Section
from backend.meeting_time import MeetingTime


def create_sample_courses():
    # CS101
    cs101 = Course("CS101", "Introduction to Programming")

    cs101.add_section(
        Section("CS101", "A",
                MeetingTime("Mon", "09:00", "10:00"),
                "Dr. Smith")
    )

    cs101.add_section(
        Section("CS101", "B",
                MeetingTime("Tue", "09:00", "10:00"),
                "Dr. Johnson")
    )

    cs101.add_section(
        Section("CS101", "C",
                MeetingTime("Thu", "13:00", "14:00"),
                "Dr. Lee")
    )

    # MATH201
    math201 = Course("MATH201", "Calculus I")

    math201.add_section(
        Section("MATH201", "A",
                MeetingTime("Mon", "09:00", "10:00"),
                "Dr. Brown")
    )

    math201.add_section(
        Section("MATH201", "B",
                MeetingTime("Wed", "11:00", "12:00"),
                "Dr. Green")
    )

    math201.add_section(
        Section("MATH201", "C",
                MeetingTime("Fri", "09:00", "10:00"),
                "Dr. Davis")
    )

    # PHYS150
    phys150 = Course("PHYS150", "Physics I")

    phys150.add_section(
        Section("PHYS150", "A",
                MeetingTime("Tue", "09:00", "10:00"),
                "Dr. White")
    )

    phys150.add_section(
        Section("PHYS150", "B",
                MeetingTime("Thu", "14:00", "15:00"),
                "Dr. Black")
    )

    phys150.add_section(
        Section("PHYS150", "C",
                MeetingTime("Fri", "14:00", "15:00"),
                "Dr. Miller")
    )

    return [cs101, math201, phys150]

def get_course_names():
    """Return a list of all available course codes."""
    return [course.course_code for course in create_sample_courses()]


def get_courses_by_codes(course_codes):
    """
    Return Course objects matching the selected course codes.

    Example:
        get_courses_by_codes(["CS101", "PHYS150"])
    """
    all_courses = create_sample_courses()
    return [course for course in all_courses if course.course_code in course_codes]