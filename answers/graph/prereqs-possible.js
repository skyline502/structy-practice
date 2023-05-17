const prereqsPossible = (numCourses, prereqs) => {
    let courses = {};
    let visiting = new Set();
    let visited = new Set();

    for (let course of prereqs) {
        if (!courses[course[0]]) {
            courses[course[0]] = [course[1]];
        } else {
            courses[course[0]].push(course[1]);
        }

        if (!courses[course[1]]) {
            courses[course[1]] = [];
        }
    }

    for (let course in courses) {
        if (hasCycle(courses, course, visiting, visited)) {
            return false;
        }
    }

    return true;
}

const hasCycle = (courses, node, visiting, visited) => {
    if (visited.has(node)) return false;

    if (visiting.has(node)) return true;

    visiting.add(node);

    for (let neighbor of courses[node]) {
        if (hasCycle(courses, neighbor, visiting, visited)) {
            return true;
        }
    }

    visiting.delete(node);
    visited.add(node);

    return false;

}
