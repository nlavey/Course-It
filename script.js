import {createCourse} from "./js/course.js";
import {loadCourses} from "./js/storage.js";
import {saveCourses} from "./js/storage.js";
import {renderCourses} from "./js/ui.js";

let courses = loadCourses();

renderCourses(courses);

const addBtn =
document.getElementById("addBtn");

document.getElementById("courseName").value="";

document.getElementById("units").value="";

addBtn.addEventListener("click",()=>{

    const name =
        document.getElementById("courseName").value;

    const units =
        document.getElementById("units").value;

    if(!name) return;

    const course =
        createCourse(name,units);

    courses.push(course);

    saveCourses(courses);

    renderCourses(courses);

});

document
.getElementById("courseList")
.addEventListener("click",(e)=>{

    if(e.target.tagName!=="BUTTON") return;

    const id=Number(
        e.target.dataset.id
    );

    courses=courses.filter(
        c=>c.id!==id
    );

    saveCourses(courses);

    renderCourses(courses);

});