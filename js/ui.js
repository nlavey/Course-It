import {
    getCompletedTopics,
    getProgressPercent
} from "./progress.js";

import { formatPercent } from "./utils.js";

export function renderCourse(course) {

    document.getElementById("courseName").value =
        course.name;

    document.getElementById("instructor").value =
        course.instructor;
}

export function renderTopics(course, handlers) {

    const list = document.getElementById("topicList");

    const topicCount =
        document.getElementById("topicCount");

    list.innerHTML = "";

    topicCount.textContent =
        `${course.topics.length} Topic${course.topics.length === 1 ? "" : "s"}`;

    if (course.topics.length === 0) {

        list.innerHTML =
            `<li class="empty">No topics yet.</li>`;

        return;
    }

    course.topics.forEach(topic => {

        const li = document.createElement("li");

        const left = document.createElement("div");

        const checkbox =
            document.createElement("input");

        checkbox.type = "checkbox";
        checkbox.checked = topic.completed;

        checkbox.addEventListener("change", () => {
            handlers.toggle(topic.id);
        });

        const title =
            document.createElement("span");

        title.textContent = topic.title;

        if (topic.completed) {
            title.style.textDecoration =
                "line-through";
            title.style.color = "#888";
        }

        title.addEventListener("dblclick", () => {

            const updated =
                prompt(
                    "Edit Topic",
                    topic.title
                );

            if (updated !== null) {
                handlers.edit(
                    topic.id,
                    updated
                );
            }

        });

        left.style.display = "flex";
        left.style.alignItems = "center";
        left.style.gap = "10px";

        left.appendChild(checkbox);
        left.appendChild(title);

        const deleteButton =
            document.createElement("button");

        deleteButton.textContent = "🗑";

        deleteButton.addEventListener("click", () => {
            handlers.delete(topic.id);
        });

        li.appendChild(left);
        li.appendChild(deleteButton);

        list.appendChild(li);

    });

}

export function renderProgress(course) {

    const completed =
        getCompletedTopics(course.topics);

    const percent =
        getProgressPercent(course.topics);

    document.getElementById(
        "progressText"
    ).textContent =
        `${completed} / ${course.topics.length} Complete`;

    document.getElementById(
        "progressPercent"
    ).textContent =
        formatPercent(percent);

    document.getElementById(
        "progressFill"
    ).style.width =
        `${percent}%`;

}

export function renderApp(course, handlers) {

    renderCourse(course);

    renderTopics(course, handlers);

    renderProgress(course);

}