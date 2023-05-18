const countPaths = (grid, row = 0, col = 0, memo = {}) => {
  const node = row + ',' + col;

  if (node in memo) return memo[node];
  if (row === grid.length || col === grid[0].length || grid[row][col] === 'X') return 0;
  if (row === grid.length - 1 && col === grid[0].length - 1) return 1;

  memo[node] = countPaths(grid, row + 1, col, memo) + countPaths(grid, row, col + 1, memo);
  return memo[node];
};
