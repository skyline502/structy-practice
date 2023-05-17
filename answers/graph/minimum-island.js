const minimumIsland = (grid) => {
  let minSize = Infinity;
  let visited = new Set();
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      let size = getSize(grid, r, c, visited);
      if (size > 0 && size < minSize) {
        minSize = size;
      }
    }
  }
  return minSize;
};

const getSize = (grid, r, c, visited) => {
  let rowInbounds = 0 <= r && r < grid.length;
  let colInbounds = 0 <= c && c < grid[0].length;

  if (!rowInbounds || !colInbounds) return 0;
  if (grid[r][c] === 'W') return 0;

  let node = r + ',' + c;

  if (visited.has(node)) return 0;
  visited.add(node);
  let size = 1;


  size += getSize(grid, r - 1, c, visited);
  size += getSize(grid, r + 1, c, visited);
  size += getSize(grid, r, c - 1, visited);
  size += getSize(grid, r, c + 1, visited);

  return size;

}
