class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def display(self):
        print(f"\n{self.course_code} - {self.course_name}")

        for section in self.sections:
            print("---------------------")
            section.display()