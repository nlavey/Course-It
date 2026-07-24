from scheduler import Scheduler
from data import create_sample_courses


def test_scheduler():
    courses = create_sample_courses()

    scheduler = Scheduler(courses)
    solution = scheduler.solve()

    assert solution is not None
    assert len(solution) == len(courses)