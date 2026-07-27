from collections import defaultdict


def score(schedule, preference):

    if preference == "fewest_gaps":
        return -count_gaps(schedule)

    if preference == "latest_start":
        return latest_start(schedule)

    if preference == "earliest_finish":
        return -earliest_finish(schedule)

    if preference == "four_day_week":
        return -days_used(schedule)

    if preference == "no_friday":
        return no_friday(schedule)

    if preference == "longest_lunch":
        return lunch_length(schedule, mode="worst")

    return 0

def count_gaps(schedule):

    by_day = defaultdict(list)

    for section in schedule:
        for mt in section.meeting_times:
            by_day[mt.day].append(mt)

    gaps = 0

    for meetings in by_day.values():

        meetings.sort(key=lambda x: x.start)

        for i in range(len(meetings)-1):

            gap = meetings[i+1].start - meetings[i].end

            if gap > 0:
                gaps += gap

    return gaps

def latest_start(schedule):

    earliest = float('inf')

    for section in schedule:
        for mt in section.meeting_times:

            earliest = min(earliest, mt.start)

    return earliest if earliest != float('inf') else 0

def earliest_finish(schedule):

    latest = 0

    for section in schedule:
        for mt in section.meeting_times:
            latest = max(latest, mt.end)

    return latest

def days_used(schedule):

    days = set()

    for section in schedule:
        for mt in section.meeting_times:
            days.add(mt.day)

    return len(days)

def no_friday(schedule):

    for section in schedule:
        for mt in section.meeting_times:

            if mt.day == "Fri":
                return -1000

    return 1000

def lunch_length(schedule, mode="worst"):
    lunch_start = 720      # 12:00
    lunch_end = 780        # 1:00

    days_present = {mt.day for section in schedule for mt in section.meeting_times}

    if not days_present:
        return lunch_end - lunch_start

    free_by_day = {}
    for day in days_present:
        free = 0
        for minute in range(lunch_start, lunch_end):
            occupied = any(
                mt.day == day and mt.start <= minute < mt.end
                for section in schedule
                for mt in section.meeting_times
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