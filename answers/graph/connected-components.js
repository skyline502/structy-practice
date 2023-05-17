const connectedComponentsCount = (graph) => {
  let visited = new Set();
  let count = 0;
  for (let el in graph) {
    if (explore(graph, el, visited)) {
      count++;
    }
  }
  return count;
};

const explore = (graph, current, visited) => {
  if (visited.has(String(current))) return false;

  visited.add(String(current));

  for (let el of graph[current]) {
    explore(graph, el, visited);
  }

  return true;
}
