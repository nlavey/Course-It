def copy_domains(domains):
    """
    Copy the domain dictionary without copying Course objects.
    """
    return {
        course: sections[:]
        for course, sections in domains.items()
    }


def remove_conflicting_sections(domains, chosen_course, chosen_section):
    """
    Remove sections that conflict with the chosen section.

    Returns:
        True if every course still has at least one section.
        False if any course loses every possible section.
    """

    for course in domains:

        if course == chosen_course:
            continue

        remaining = []

        for section in domains[course]:

            if not chosen_section.conflicts_with(section):
                remaining.append(section)

        domains[course] = remaining

        if len(domains[course]) == 0:
            return False

    return True