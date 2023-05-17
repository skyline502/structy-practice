const closestCarrot = (grid, startRow, startCol) => {
   let queue = [{node: [startRow, startCol], length: 0}];
   let visited = new Set();
   while (queue.length) {
    let current = queue.shift();
    // console.log(current, 'current')
    let row = current.node[0];
    let col = current.node[1];
    // console.log(row, col, 'row and column')
    let pos = row + ',' + col;
    if (!visited.has(pos)) {
        visited.add(pos);
        // console.log(grid[row][col], 'current element!!!!!!!!');
        // if (row - 1 >= 0 && grid[row - 1][col] === 'C') return current.length + 1;
        // if (row + 1 < grid.length && grid[row + 1][col] === 'C') return current.length + 1;
        // if (col - 1 >= 0 && grid[row][col - 1] === 'C') return current.length + 1;
        // if (col + 1 < grid[0].length && grid[row][col + 1] === 'C') return current.length + 1;
        if (grid[row][col] === 'C') return current.length;

        if (row - 1 >= 0 && grid[row - 1][col] !== 'X') queue.push({node: [row - 1, col], length: current.length + 1});
        if (row + 1 < grid.length && grid[row + 1][col] !== 'X') queue.push({node: [row + 1, col], length: current.length + 1});
        if (col - 1 >= 0 && grid[row][col - 1] !== 'X') queue.push({node: [row, col - 1], length: current.length + 1});
        if (col + 1 < grid[0].length && grid[row][col + 1] !== 'X') queue.push({node: [row, col + 1], length: current.length + 1});
    }
   }

   return -1;
};
