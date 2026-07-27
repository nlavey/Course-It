from data import create_sample_courses
from scheduler import Scheduler
from preferences import Preference

courses = create_sample_courses()

scheduler = Scheduler(
    courses,
    Preference.NO_FRIDAY
)

solutions = scheduler.solve()

if solutions:

    for i, solution in enumerate(solutions, start=1):

        print("=" * 40)
        print(f"Schedule #{i}\n")

        for course, section in solution.items():
            print(section)

        print()

else:
    print("No valid schedules found.")