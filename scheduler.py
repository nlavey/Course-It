from csp_utils import copy_domains
from csp_utils import remove_conflicting_sections

class Scheduler:

    def __init__(self, courses):

        self.courses = courses

    def solve(self):

        domains = {}

        for course in self.courses:
            domains[course] = course.sections[:]

        return self.forward_check({}, domains)

    def forward_check(self, assignment, domains):

        # Finished

        if len(assignment) == len(self.courses):
            return assignment

        # Pick next unassigned course

        unassigned = []

        for course in self.courses:
            if course not in assignment:
                unassigned.append(course)

        course = unassigned[0]

        for section in domains[course]:

            new_assignment = assignment.copy()
            new_assignment[course] = section

            new_domains = copy_domains(domains)

            new_domains[course] = [section]

            valid = remove_conflicting_sections(
                new_domains,
                course,
                section
            )

            if not valid:
                continue

            result = self.forward_check(
                new_assignment,
                new_domains
            )

            if result is not None:
                return result

        return None