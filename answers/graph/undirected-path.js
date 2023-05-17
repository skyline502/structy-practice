const undirectedPath = (edges, nodeA, nodeB) => {
    let graph = {};
    for (let edge of edges) {
        if (!graph[edge[0]]) {
            graph[edge[0]] = [edge[1]];
        } else {
            graph[edge[0]].push(edge[1]);
        }
        if (!graph[edge[1]]) {
            graph[edge[1]] = [edge[0]];
        } else {
            // console.log('exists', graph[edge[1]])
            graph[edge[1]].push(edge[0]);
        }
    }
    let stack = [graph[nodeA]];
    let visited = new Set();
    console.log(stack, graph)
    while(stack.length) {
        let current = stack.pop();
        for (el of current) {
            console.log(el, 'current el');
            if (el === nodeB) return true;
            if (!visited.has(el)) {
               stack.push(graph[el]);
               visited.add(el);
            }

        }
    }
    return false;
};
