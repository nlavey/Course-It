class Section:
    def __init__(self, section_id, days, start_time, end_time, professor):
        self.section_id = section_id
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.professor = professor

    def display(self):
        print(f"Section {self.section_id}")
        print(f"Professor: {self.professor}")
        print(f"Days: {', '.join(self.days)}")
        print(f"Time: {self.start_time} - {self.end_time}")