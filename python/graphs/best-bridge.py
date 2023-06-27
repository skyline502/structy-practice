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
    print(pos, 'current pos')


def is_inbounds(grid, row, col):
  row_inbounds = row >= 0 and row < len(grid)
  col_inbounds = 0 <= col and col < len(grid[0])

  print(row_inbounds, 'rows', row, col)
  print(col_inbounds, 'col', row, col)

  return row_inbounds and col_inbounds



def find_island(grid, row, col, visited):
  if is_inbounds(grid, row, col) == False or grid[row][col] == 'W':
    return visited

  node = str(row) + ',' + str(col)

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
