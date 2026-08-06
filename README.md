# Course It

A desktop application that generates conflict-free university class schedules using **Constraint Satisfaction Problem (CSP)** techniques. Users can load real course catalogs from CSV files, search for courses, specify scheduling preferences, and browse multiple ranked schedules in an interactive weekly calendar.

---

## Features

* Generates valid schedules using a **backtracking CSP solver**.
* Uses **forward checking** to prune invalid choices and improve performance.
* Produces multiple valid schedules ranked by user preferences.
* Supports scheduling preferences including:

  * Fewest gaps between classes
  * Latest start times
  * Earliest finish times
  * Four-day schedules
  * No Friday classes
  * Longest lunch break
* Loads complete course catalogs from CSV files.
* Supports multiple semesters.
* Live course search.
* Interactive weekly calendar visualization.
* Browse the top generated schedules with Previous/Next navigation.
* Consistent course colors across schedules.

---

## Technologies

* Python 3
* Tkinter
* Constraint Satisfaction Problems (CSP)
* Backtracking Search
* Forward Checking
* CSV Data Processing
* Object-Oriented Programming

---

## Project Structure

```text
course_scheduler/
│
├── backend/
│   ├── scheduler.py
│   ├── ranking.py
│   ├── preferences.py
│   ├── course.py
│   ├── section.py
│   ├── meeting_time.py
│   ├── data_loader.py
│   └── ...
│
├── frontend/
│   ├── app.py
│   ├── sidebar.py
│   ├── calendar_view.py
│   └── ...
│
├── data/
│   └── data.csv
│
├── main.py
└── README.md
```

---

## How It Works

Each requested course is treated as a variable in a Constraint Satisfaction Problem.

* **Variables:** Courses selected by the user
* **Domains:** Available sections for each course
* **Hard Constraints:**

  * No overlapping meeting times
  * One section per course
* **Soft Constraints:**

  * User scheduling preferences used for ranking

The solver performs a backtracking search while using forward checking to eliminate invalid assignments early. After all valid schedules are found, they are scored and ranked according to the selected preference.

---

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd course_scheduler
```

Run the application:

```bash
python main.py
```

---

## Example Workflow

1. Load a semester course catalog.
2. Search for desired courses.
3. Select courses.
4. Choose a scheduling preference.
5. Generate schedules.
6. Browse the highest-ranked schedules in the weekly calendar.

---

## Future Improvements

* Instructor preferences
* Credit-hour constraints
* Export schedules to PDF
* Export schedules to iCalendar (.ics)
* Save and reload schedules
* More advanced CSP heuristics (MRV and Least Constraining Value)

---

## License

This project is licensed under the MIT License.
