from typing import List

class Scheduler:

    def __init__(self, courses):
        self.courses = courses

    def solve(self):
        """
        Returns a list of chosen sections,
        or None if no valid schedule exists.
        """
        return self._backtrack(0, [])

    def _backtrack(self, course_index, chosen_sections):

        if course_index == len(self.courses):
            return chosen_sections.copy()

        current_course = self.courses[course_index]

        for section in current_course.sections:

            if self._is_valid(section, chosen_sections):

                chosen_sections.append(section)

                result = self._backtrack(
                    course_index + 1,
                    chosen_sections
                )

                if result is not None:
                    return result

                # Undo the choice
                chosen_sections.pop()

        return None

    def _is_valid(self, new_section, chosen_sections):

        for existing in chosen_sections:

            if new_section.conflicts_with(existing):
                return False

        return True