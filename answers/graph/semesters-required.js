const semestersRequired = (numCourses, prereqs) => {
    let graph = {};
    let visited = new Set();
    let semesters = 1;

    for (let prereq of prereqs) {
        if (!graph[prereq[0]]) {
            graph[prereq[0]] = [prereq[1]];
        } else {
            graph[prereq[0]].push(prereq[1]);
        }
        if (!graph[prereq[1]]) {
            graph[prereq[1]] = [];
        }
    }

    console.log(graph)
    for (let course in graph) {
        if (!visited.has(course)) {
            let numSems = getSems(graph, course, visited);
            if (semesters < numSems) {
                semesters = numSems;
            }
        }
    }

    return semesters;

};

let getSems = (graph, course, visited) => {
    let numSems = 1;
    let stack = [graph[course]];
    while(stack.length) {
        let current = stack.pop();
        if (current.length) {
            numSems++;
        }
        for (let c of current) {
         stack.push(graph[c]);
        }
    }
    return numSems;
}
