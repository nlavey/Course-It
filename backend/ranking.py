from collections import defaultdict

from backend.preferences import Preference


def _sections_from_schedule(schedule):
    if isinstance(schedule, dict):
        return list(schedule.values())
    return list(schedule)


def score(schedule, preference):
    sections = _sections_from_schedule(schedule)

    if preference == Preference.FEWEST_GAPS:
        return -count_gaps(sections)

    if preference == Preference.LATEST_START:
        return latest_start(sections)

    if preference == Preference.EARLIEST_FINISH:
        return -earliest_finish(sections)

    if preference == Preference.FOUR_DAY_WEEK:
        return -days_used(sections)

    if preference == Preference.NO_FRIDAY:
        return no_friday(sections)

    if preference == Preference.LONGEST_LUNCH:
        return lunch_length(sections, mode="worst")

    return 0


def count_gaps(schedule):
    by_day = defaultdict(list)

    for section in _sections_from_schedule(schedule):
        mt = section.meeting_time
        by_day[mt.day].append(mt)

    gaps = 0

    for meetings in by_day.values():

        meetings.sort(key=lambda m: m.start)

        for i in range(len(meetings) - 1):

            gap = meetings[i + 1].start - meetings[i].end

            if gap > 0:
                gaps += gap

    return gaps

def latest_start(schedule):
    first_class = float("inf")

    for section in _sections_from_schedule(schedule):
        first_class = min(first_class, section.meeting_time.start)

    return first_class if first_class != float("inf") else 0

def earliest_finish(schedule):
    latest = 0

    for section in _sections_from_schedule(schedule):
        latest = max(latest, section.meeting_time.end)

    return latest

def days_used(schedule):
    days = set()

    for section in _sections_from_schedule(schedule):
        days.add(section.meeting_time.day)

    return len(days)

def no_friday(schedule):
    for section in _sections_from_schedule(schedule):
        if section.meeting_time.day == "Fri":
            return -1000

    return 1000

def lunch_length(schedule, mode="worst"):
    lunch_start = 720      # 12:00
    lunch_end = 780        # 1:00

    days_present = {
        section.meeting_time.day
        for section in _sections_from_schedule(schedule)
    }

    if not days_present:
        return lunch_end - lunch_start

    free_by_day = {}
    for day in days_present:
        free = 0
        for minute in range(lunch_start, lunch_end):
            occupied = any(
                section.meeting_time.day == day
                and section.meeting_time.start <= minute < section.meeting_time.end
                for section in _sections_from_schedule(schedule)
            )
            if not occupied:
                free += 1
        free_by_day[day] = free

    if mode == "worst":
        return min(free_by_day.values())
    elif mode == "average":
        return sum(free_by_day.values()) / len(free_by_day)
    elif mode == "sum":
        return sum(free_by_day.values())
    else:
        raise ValueError(f"Unknown mode: {mode}")