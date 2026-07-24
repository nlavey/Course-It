from data import create_sample_courses
from scheduler import Scheduler

courses = create_sample_courses()

scheduler = Scheduler(courses)

solution = scheduler.solve()

if solution is None:
    print("No valid schedule found.")

else:
    print("Valid Schedule")

    for section in solution:
        print(section)