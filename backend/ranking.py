from collections import defaultdict

from backend.preferences import Preference


def _sections_from_schedule(schedule):
    if isinstance(schedule, dict):
        return list(schedule.values())
    return list(schedule)


def _all_meeting_times(schedule):
    for section in _sections_from_schedule(schedule):
        for mt in getattr(section, "meeting_times", []):
            if mt is not None:
                yield mt


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

    for mt in _all_meeting_times(schedule):
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

    for mt in _all_meeting_times(schedule):
        first_class = min(first_class, mt.start)

    return first_class if first_class != float("inf") else 0


def earliest_finish(schedule):
    latest = 0

    for mt in _all_meeting_times(schedule):
        latest = max(latest, mt.end)

    return latest


def days_used(schedule):
    days = {mt.day for mt in _all_meeting_times(schedule)}
    return len(days)


def no_friday(schedule):
    for mt in _all_meeting_times(schedule):
        if mt.day == "Fri":
            return -1000

    return 1000


def lunch_length(schedule, mode="worst"):
    lunch_start = 720      # 12:00
    lunch_end = 780        # 1:00

    days_present = {mt.day for mt in _all_meeting_times(schedule)}

    if not days_present:
        return lunch_end - lunch_start

    free_by_day = {}
    meetings = list(_all_meeting_times(schedule))

    for day in days_present:
        free = 0
        for minute in range(lunch_start, lunch_end):
            occupied = any(
                mt.day == day and mt.start <= minute < mt.end
                for mt in meetings
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
