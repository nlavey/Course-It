const KEY = "courses";

export function loadCourses(){

    return JSON.parse(localStorage.getItem(KEY)) || [];

}

export function saveCourses(courses){

    localStorage.setItem(
        KEY,
        JSON.stringify(courses)
    );

}