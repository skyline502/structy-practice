# level averages

# Write a function, levelAverages, that takes in the root of a binary tree that
# contains number values. The function should return an array containing the average
# value of each level.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def levelAverages(root):
  if root == None:
    return []
  levels = []
  queue = [[root, 0]]

  while len(queue) > 0:
    current = queue.pop(0)
    node = current[0]
    level = current[1]

    if len(levels) <= level:
      levels.append([node.val])
    else:
      levels[level].append(node.val)

    if node.left and node.left != None:
      queue.append([node.left, level + 1])

    if node.right and node.right != None:
      queue.append([node.right, level + 1])

  level_avg = []

  for arr in levels:
    total = 0
    for num in arr:
      total += num
    level_avg.append(total/len(arr))

  return level_avg


# Examples:

# test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(levelAverages(a)) # -> [ 3, 7.5, 1 ]
# test_01:
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

# #        5
# #     /    \
# #    11    54
# #  /   \
# # 20   15
# #      / \
# #     1  3

print(levelAverages(a)) # -> [ 5, 32.5, 17.5, 2 ]
# # test_02:
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(45)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   0     45
# #     /       \
# #    -1       -2

print(levelAverages(a)) # -> [ -1, -5.5, 14, -1.5 ]
# # test_03:
q = Node(13)
r = Node(4)
s = Node(2)
t = Node(9)
u = Node(2)
v = Node(42)

q.left = r
q.right = s
r.right = t
t.left = u
u.right = v

# #        13
# #      /   \
# #     4     2
# #      \
# #       9
# #      /
# #     2
# #    /
# #   42

print(levelAverages(q)) # -> [ 13, 3, 9, 2, 42 ]
# # test_04:
print(levelAverages(None)) # -> [ ]
