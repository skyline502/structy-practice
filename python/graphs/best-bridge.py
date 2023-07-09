# best bridge

# Write a function, print(bestBridge, that) takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid.
# An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands.
# A bridge does not need to form a straight line.

def bestBridge(grid):
  island = None
  visited = set()
  for row, rows in enumerate(grid):
   for col, column in enumerate(rows):
    possible_island = find_island(grid, row, col, set())

    if len(possible_island) > 0:
      print(possible_island, 'island found')
      island = possible_island
      break

  visited = set()
  queue = []

  for pos in island:
    [row, col] = pos.split(',')
    queue.append([row, col, 0])

  while len(queue) > 0:
    [row, col, distance] = queue.pop(0)

    pos = str(row) + ',' + str(col)

    if grid[int(row)][int(col)] == 'L' and pos not in island:
      return distance - 1

    deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for delta in deltas:
      [delta_row, delta_col] = delta
      neighbor_row = int(row) + delta_row
      neighbor_col = int(col) + delta_col
      neighbor_pos = str(neighbor_row) + ',' + str(neighbor_col)

      if is_inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
        visited.add(neighbor_pos)
        queue.append([neighbor_row, neighbor_col, distance + 1])


def is_inbounds(grid, row, col):
  row_inbounds = True if row >= 0 and row < len(grid) else False
  col_inbounds = True if 0 <= col and col < len(grid[0]) else False

  if row_inbounds == True and col_inbounds == True:
    return True
  else:
    return False



def find_island(grid, row, col, visited):
  if is_inbounds(grid, row, col) == False or grid[row][col] == 'W':
    # print('not an island')
    return visited

  node = str(row) + ',' + str(col)

  if node in visited:
    return visited

  visited.add(node)

  find_island(grid, row + 1, col, visited)
  find_island(grid, row - 1, col, visited)
  find_island(grid, row, col + 1, visited)
  find_island(grid, row, col - 1, visited)

  return visited

# test_00:

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
print(bestBridge(grid)) # -> 1

# test_01:

# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["L", "L", "W", "W", "L"],
#   ["W", "L", "W", "W", "L"],
#   ["W", "W", "W", "L", "L"],
#   ["W", "W", "W", "W", "W"],
# ]
# print(bestBridge(grid)) # -> 2

# # test_02:

# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "L", "W"],
#   ["L", "W", "W", "W", "W"],
# ]
# print(bestBridge(grid)) # -> 3

# # test_03:

# grid = [
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "L", "W", "W"],
#   ["W", "W", "W", "W", "L", "L", "W", "W"],
#   ["W", "W", "W", "W", "L", "L", "L", "W"],
#   ["W", "W", "W", "W", "W", "L", "L", "L"],
#   ["L", "W", "W", "W", "W", "L", "L", "L"],
#   ["L", "L", "L", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
# ]
# print(bestBridge(grid)) # -> 3

# # test_04:

# grid = [
#   ["L", "L", "L", "L", "L", "L", "L", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "L", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "L", "L", "L", "L", "L", "L", "L"],
# ]
# print(bestBridge(grid)) # -> 2

# # test_05:

# grid = [
#   ["W", "L", "W", "W", "W", "W", "W", "W"],
#   ["W", "L", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "L", "W"],
#   ["W", "W", "W", "W", "W", "W", "L", "L"],
#   ["W", "W", "W", "W", "W", "W", "W", "L"],
# ]
# print(bestBridge(grid)) # -> 8
