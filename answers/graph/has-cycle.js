const hasCycle = (list) => {
    let visited = new Set();
    let visiting = new Set();

    for (let node in list) {
        if (findCycle(list, node, visiting, visited)) {//if findCycle returns true, return true;
            return true;
        }
    }

    return false; //if no cycle is found
}

const findCycle = (list, node, visiting, visited) => {
    if (visited.has(node)) return false; //that means we have visited everything and no cycle is found
    if (visiting.has(node)) return true; //if visiting already has node, that means we are visiting the node again, thus a cycle

    visiting.add(node);

    for (let neighbor of list[node]) { //checks all the neighbors of current node, and we run the findCycle on each neighbor
        if (findCycle(list, neighbor, visiting, visited)) return true;
    }

    visiting.delete(node); //we delete the node from visiting after we complete the for loop for all of its neighbors
    visited.add(node); //then we add the node to the visited list
    return false;
}
