const shortestPath = (edges, nodeA, nodeB) => {
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
          graph[edge[1]].push(edge[0]);
        }
    }

    let queue = [{node: nodeA, length: 0}];
    let visited = new Set();
    while (queue.length) {
      let current = queue.pop();
      if (current.node === nodeB) return current.length;
      for (let el of graph[current.node]) {
        if (!visited.has(el)){
          queue.unshift({node: el, length: current.length + 1})
          visited.add(el);
        }
      }
    }
    return -1;
};
