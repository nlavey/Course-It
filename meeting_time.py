class MeetingTime:
    def __init__(self, days, start, end):
        self.days = days
        self.start = self.time_to_minutes(start)
        self.end = self.time_to_minutes(end)

    @staticmethod
    def time_to_minutes(time_string):
        hour, minute = map(int, time_string.split(":"))
        return hour * 60 + minute

    def shares_day(self, other):
        return any(day in other.days for day in self.days)

    def overlaps(self, other):
        return self.start < other.end and other.start < self.end

    def __str__(self):
        return f"{self.days} {self.start}-{self.end}"