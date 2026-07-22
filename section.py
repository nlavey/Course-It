class Section:
    def __init__(self, course_code, section_id, meeting_time, instructor):
        self.course_code = course_code
        self.section_id = section_id
        self.meeting_time = meeting_time
        self.instructor = instructor

    def conflicts_with(self, other):
        if not self.meeting_time.shares_day(other.meeting_time):
            return False

        return self.meeting_time.overlaps(other.meeting_time)

    def __str__(self):
        return (
            f"{self.course_code} "
            f"{self.section_id} "
            f"{self.meeting_time}"
        )