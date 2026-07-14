import { loadCourse, saveCourse } from "./storage.js";

import {
    createCourse,
    updateCourseInfo,
    addTopic,
    deleteTopic,
    toggleTopic,
    editTopic
} from "./course.js";

import { renderApp } from "./ui.js";

let course = loadCourse();

if (!course) {
    course = createCourse();
}

function refresh() {
    saveCourse(course);

    renderApp(course, {
        toggle: handleToggleTopic,
        delete: handleDeleteTopic,
        edit: handleEditTopic
    });
}

function handleSaveCourse() {

    const name =
        document.getElementById("courseName").value;

    const instructor =
        document.getElementById("instructor").value;

    updateCourseInfo(
        course,
        name,
        instructor
    );

    refresh();

}

function handleAddTopic() {

    const input =
        document.getElementById("topicInput");

    addTopic(
        course,
        input.value
    );

    input.value = "";

    refresh();

}

function handleDeleteTopic(id) {

    deleteTopic(
        course,
        id
    );

    refresh();

}

function handleToggleTopic(id) {

    toggleTopic(
        course,
        id
    );

    refresh();

}

function handleEditTopic(id, title) {

    editTopic(
        course,
        id,
        title
    );

    refresh();

}

document
    .getElementById("saveCourse")
    .addEventListener(
        "click",
        handleSaveCourse
    );

document
    .getElementById("addTopic")
    .addEventListener(
        "click",
        handleAddTopic
    );

document
    .getElementById("topicInput")
    .addEventListener(
        "keydown",
        event => {

            if (event.key === "Enter") {
                handleAddTopic();
            }

        }
    );

refresh();