from data import create_sample_courses
from scheduler import Scheduler


def test_scheduler():

    courses = create_sample_courses()

    scheduler = Scheduler(courses)

    result = scheduler.solve()

    assert result is not None

    sections = list(result.values())

    for i in range(len(sections)):
        for j in range(i + 1, len(sections)):
            assert not sections[i].conflicts_with(sections[j])


if __name__ == "__main__":
    test_scheduler()
    print("Forward checking test passed.")