from course import Course
from section import Section

cse30 = Course("CSE30", "Programming Abstractions")

cse30.add_section(
    Section(
        "01",
        ["Mon", "Wed"],
        "9:20",
        "10:55",
        "Harrison"
    )
)

cse30.add_section(
    Section(
        "02",
        ["Tue", "Thu"],
        "2:00",
        "3:35",
        "Lee"
    )
)

math19b = Course("MATH19B", "Calculus II")

math19b.add_section(
    Section(
        "01",
        ["Mon", "Wed", "Fri"],
        "11:40",
        "12:45",
        "Kim"
    )
)

math19b.add_section(
    Section(
        "02",
        ["Tue", "Thu"],
        "8:00",
        "9:35",
        "Smith"
    )
)

courses = [cse30, math19b]