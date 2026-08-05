class Section:
    def __init__(self, course_code, section_id, meeting_times, instructor):
        self.course_code = course_code
        self.section_id = section_id

        if meeting_times is None:
            self.meeting_times = []
        elif isinstance(meeting_times, list):
            self.meeting_times = meeting_times
        else:
            self.meeting_times = [meeting_times]

        self.meeting_time = self.meeting_times[0] if self.meeting_times else None
        self.instructor = instructor

    def conflicts_with(self, other):
        for mt1 in self.meeting_times:
            for mt2 in other.meeting_times:
                if mt1.shares_day(mt2) and mt1.overlaps(mt2):
                    return True
        return False

    def __str__(self):
        meeting_str = ", ".join(str(mt) for mt in self.meeting_times)
        return (
            f"{self.course_code} {self.section_id} | "
            f"{self.instructor} | "
            f"{meeting_str}"
        )