from data import create_sample_courses
from scheduler import Scheduler

courses = create_sample_courses()

scheduler = Scheduler(courses)

solution = scheduler.solve()

if solution:

    print("Valid Schedule\n")

    for course, section in solution.items():
        print(section)

else:
    print("No valid schedule found.")