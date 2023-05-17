const bestBridge = (grid) => {
    //find land
    let island;

    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            // console.log(r, c, 'current node')
            let possibleIsland = exploreIsland(grid, r, c, new Set()); //finds first island
            if (possibleIsland.size > 0) { //if an island is found, it breaks out of the loop;
                console.log(possibleIsland, 'possible island found')
                island = possibleIsland;
                break;
            }
        }
    }

    const visited = new Set(island);
    const queue = [];
    for (let pos of island) {
        console.log(pos, 'current position')
        const [row, col] = pos.split(',').map(Number);
        console.log('row:', row, 'col:', col)
        queue.push([row, col, 0]);
    }
    console.log(queue, 'current queue')
    while (queue.length > 0) {
        const [row, col, distance] = queue.shift();

        const pos = row + ',' + col;
        if (grid[row][col] === 'L' && !island.has(pos)) return distance - 1; //checks the neighbors, and if it is land, we have found the other island

        const deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for (let delta of deltas) {
            const [deltaRow, deltaCol] = delta;
            const neighborRow = row + deltaRow;
            const neighborCol = col + deltaCol;
            const neighborPos = neighborRow + ',' + neighborCol;
            if (isInbounds(grid, neighborRow, neighborCol) && !visited.has(neighborPos)) { //adds neighbors of the main nodes of the main island to the queue;
                visited.add(neighborPos);
                queue.push([neighborRow, neighborCol, distance + 1]);
            }
        }
    }
};

const isInbounds = (grid, row, col) => {
    const rowInbounds = 0 <= row && row < grid.length;
    const colInbounds = 0 <= col && col < grid[0].length;
    return rowInbounds && colInbounds;
};


let exploreIsland = (grid, r, c, visited) => {

    if (!isInbounds(grid, r, c) || grid[r][c] === 'W') return visited;

    let node = r + ',' + c;
    if (visited.has(node)) return visited;
    // console.log(node, 'node is')
    visited.add(node);
    exploreIsland(grid, r + 1, c, visited);
    exploreIsland(grid, r - 1, c, visited);
    exploreIsland(grid, r, c + 1, visited);
    exploreIsland(grid, r, c - 1, visited);

    return visited;
}
