export function createCourse(name, units){

    return{

        id:Date.now(),

        name,

        units

    };

}