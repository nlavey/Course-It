class Preference:

    FEWEST_GAPS = "fewest_gaps"

    LATEST_START = "latest_start"

    EARLIEST_FINISH = "earliest_finish"

    FOUR_DAY_WEEK = "four_day_week"

    NO_FRIDAY = "no_friday"

    LONGEST_LUNCH = "longest_lunch"

    ALL = [
        FEWEST_GAPS,
        LATEST_START,
        EARLIEST_FINISH,
        FOUR_DAY_WEEK,
        NO_FRIDAY,
        LONGEST_LUNCH,
    ]

    LABELS = {
        FEWEST_GAPS: "Fewest Gaps",
        LATEST_START: "Latest Start",
        EARLIEST_FINISH: "Earliest Finish",
        FOUR_DAY_WEEK: "Four-Day Week",
        NO_FRIDAY: "No Friday",
        LONGEST_LUNCH: "Longest Lunch",
    }