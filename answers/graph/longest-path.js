const longestPath = (graph) => {
   let longest = 0;
   let visited = new Set();
   for (let node in graph) {
     let size = getPath(graph, node, visited);
     if (size > longest) {
        longest = size;
     }
   }

   return longest;
}

const getPath = (graph, node, visited) => {
    let size = 0;
    let stack = [graph[node]];
    while (stack.length) {
        let current = stack.pop();
        if (current.length) {
            size++;
        }
        for (let node of current) {
            if (!visited.has(node)) {
                visited.add(node);
                stack.push(graph[node]);
            }
        }
    }

    return size;
}
