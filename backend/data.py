from backend.data_loader import load_catalog

_CATALOG_COURSES = None


def create_sample_courses():
    courses = load_catalog("data.csv")
    set_catalog(courses)
    return courses


def set_catalog(courses):
    global _CATALOG_COURSES
    _CATALOG_COURSES = list(courses)
    return _CATALOG_COURSES


def load_catalog_from_path(path):
    courses = load_catalog(path)
    return set_catalog(courses)


def get_available_courses():
    global _CATALOG_COURSES
    if _CATALOG_COURSES is None:
        return create_sample_courses()
    return _CATALOG_COURSES


def get_course_names():
    """Return a list of all available course codes."""
    return [course.course_code for course in get_available_courses()]


def get_courses_by_codes(course_codes):
    """
    Return Course objects matching the selected course codes.

    Example:
        get_courses_by_codes(["CS101", "PHYS150"])
    """
    all_courses = get_available_courses()
    return [course for course in all_courses if course.course_code in course_codes]