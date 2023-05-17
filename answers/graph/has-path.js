const hasPath = (graph, src, dst) => {
    let stack = [graph[src]];
    while (stack.length) {
        let current = stack.pop();
        for (let el of current) {
            if (el === dst) return true;
            stack.push(graph[el]);
        }
    }
    return false;
};
