# tree path finder

# Write a function, pathFinder, that takes in the root of a
# binary tree and a target value. The function should return
# an array representing a path to the target value. If the target
# value is not found in the tree, then return null.

# You may assume that the tree contains unique values.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def pathFinder(root, target):
  if root == None:
    return None
  print(root.val, target)

# Examples:
# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(pathFinder(a, 'e')) # -> [ 'a', 'b', 'e' ]
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# print(pathFinder(a, 'p')) # -> null
# # test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# print(pathFinder(a, "c")) # -> ['a', 'c']
# # test_03:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# print(pathFinder(a, "h")) # -> ['a', 'c', 'f', 'h']
# test_04:
x = Node("x")

#      x

print(pathFinder(x, "x")) # -> ['x']
# test_05:
print(pathFinder(None, "x")) # -> null
# test_06:
# root = Node(0)
# let curr = root
# for (let i = 1 i <= 6000 i += 1) {
#   curr.right = Node(i)
#   curr = curr.right
# }

# #      0
# #       \
# #        1
# #         \
# #          2
# #           \
# #            3
# #             .
# #              .
# #               .
# #              5999
# #                \
# #                6000

# print(pathFinder(root, 3451)) # -> [0, 1, 2, 3, ..., 3450, 3451]
