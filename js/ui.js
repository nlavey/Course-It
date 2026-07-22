export function renderCourses(courses){

    const list =
        document.getElementById("courseList");

    list.innerHTML="";

    courses.forEach(course=>{

        const li=document.createElement("li");

        li.innerHTML=`
            ${course.name}
            (${course.units} units)

            <button data-id="${course.id}">
                Delete
            </button>
        `;

        list.appendChild(li);

    });

}