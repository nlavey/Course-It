from backend.data import create_sample_courses
from backend.scheduler import Scheduler


class Controller:

    def generate_schedule(self, selected_codes):

        all_courses = create_sample_courses()

        selected = [
            course
            for course in all_courses
            if course.code in selected_codes
        ]

        scheduler = Scheduler(selected)

        return scheduler.solve()