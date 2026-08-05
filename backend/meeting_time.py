class MeetingTime:
    DAY_TOKEN_MAP = {
        "M": "Mon",
        "Mon": "Mon",
        "Tu": "Tue",
        "Tue": "Tue",
        "W": "Wed",
        "Wed": "Wed",
        "Th": "Thu",
        "Thu": "Thu",
        "F": "Fri",
        "Fri": "Fri",
    }

    def __init__(self, days, start, end):
        parsed_days = self._parse_days(days)
        self.days = parsed_days
        self.day = parsed_days[0] if parsed_days else None
        self.start = self.time_to_minutes(start)
        self.end = self.time_to_minutes(end)

    @staticmethod
    def time_to_minutes(time_string):
        hour, minute = map(int, time_string.split(':'))
        return hour * 60 + minute

    @classmethod
    def _parse_days(cls, days_string):
        if isinstance(days_string, list):
            return [cls.DAY_TOKEN_MAP.get(token, token) for token in days_string if token]

        days_string = str(days_string).strip()
        if not days_string:
            return []

        if ',' in days_string or ' ' in days_string:
            tokens = [token.strip() for token in days_string.replace(',', ' ').split() if token.strip()]
            return [cls.DAY_TOKEN_MAP.get(token, token) for token in tokens]

        days = []
        index = 0
        while index < len(days_string):
            if days_string.startswith('Th', index):
                days.append(cls.DAY_TOKEN_MAP['Th'])
                index += 2
            elif days_string.startswith('Tu', index):
                days.append(cls.DAY_TOKEN_MAP['Tu'])
                index += 2
            else:
                token = days_string[index]
                days.append(cls.DAY_TOKEN_MAP.get(token, token))
                index += 1

        return days

    def shares_day(self, other):
        return any(day in other.days for day in self.days)

    def overlaps(self, other):
        return self.start < other.end and other.start < self.end

    def __str__(self):
        return f"{','.join(self.days)} {self.start}-{self.end}"
