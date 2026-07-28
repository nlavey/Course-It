from backend.csp_utils import copy_domains
from backend.csp_utils import remove_conflicting_sections
from backend.ranking import score


class SolutionList(list):
    def values(self):
        if not self:
            return []

        first_solution = self[0]
        if isinstance(first_solution, dict):
            return list(first_solution.values())

        return []


class Scheduler:

    def __init__(self, courses, preference=None):

        self.courses = courses
        self.preference = preference

    def solve(self):

        domains = {}

        for course in self.courses:
            domains[course] = course.sections[:]

        solutions = SolutionList()

        self.forward_check(
            {},
            domains,
            solutions
        )

        solutions.sort(
            key=lambda s: score(s, self.preference),
            reverse=True
        )

        return SolutionList(solutions[:10])

    def forward_check(self, assignment, domains, solutions):

        # Finished

        if len(assignment) == len(self.courses):

            solutions.append(
                assignment.copy()
            )

            return

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

            self.forward_check(
                new_assignment,
                new_domains,
                solutions
            )

        return