const STORAGE_KEY = "courseItCourse";

export function loadCourse() {
    const savedCourse = localStorage.getItem(STORAGE_KEY);

    if (!savedCourse) {
        return null;
    }

    try {
        return JSON.parse(savedCourse);
    } catch (error) {
        console.error("Unable to load course:", error);
        return null;
    }
}

export function saveCourse(course) {
    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(course)
    );
}

export function clearCourse() {
    localStorage.removeItem(STORAGE_KEY);
}