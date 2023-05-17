const largestComponent = (graph) => {
  let largest = 0; //set to 0
  let visited = new Set();
  for (let node in graph) {
    const size = getSize(graph, node, visited); //we want the size of each component
    if (size > largest) {
      largest = size;
    }
  }
  return largest;
};

const getSize = (graph, node, visited) => {
  if (visited.has(node)) return 0; //if we have already visited this node, we return 0;

  visited.add(node);

  let size = 1; //it is 1 because we just added the first node
  for (let neighbor of graph[node]) {
    size += getSize(graph, neighbor, visited);
  }
  return size;
}
