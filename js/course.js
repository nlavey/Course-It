import { generateId } from "./utils.js";

export function createCourse(name = "", instructor = "") {
    return {
        name,
        instructor,
        topics: []
    };
}

export function updateCourseInfo(course, name, instructor) {
    course.name = name.trim();
    course.instructor = instructor.trim();
}

export function addTopic(course, title) {

    const topicTitle = title.trim();

    if (!topicTitle) {
        return;
    }

    course.topics.push({
        id: generateId(),
        title: topicTitle,
        completed: false
    });
}

export function deleteTopic(course, id) {
    course.topics = course.topics.filter(
        topic => topic.id !== id
    );
}

export function toggleTopic(course, id) {

    const topic = course.topics.find(
        topic => topic.id === id
    );

    if (topic) {
        topic.completed = !topic.completed;
    }
}

export function editTopic(course, id, newTitle) {

    const topic = course.topics.find(
        topic => topic.id === id
    );

    if (!topic) return;

    const title = newTitle.trim();

    if (title) {
        topic.title = title;
    }
}