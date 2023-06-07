# breadth first values

# Write a function, breadthFirstValues, that takes in the root of a binary tree.
# The function should return an array containing all values of the tree in
# breadth-first order.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadthFirstValues(root):
  queue = [root]
  values = []

  while len(queue) > 0:
    current = queue.pop(0)
    values.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return values


# Examples:

# test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

print(breadthFirstValues(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

# # test_01:

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

print(breadthFirstValues(a))
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# test_02:
# a = Node('a')

# #      a

# print(breadthFirstValues(a))
# #    -> ['a']
# # test_03:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# x = Node('x')

# a.right = b
# b.left = c
# c.left = x
# c.right = d
# d.right = e

# #      a
# #       \
# #        b
# #       /
# #      c
# #    /  \
# #   x    d
# #         \
# #          e

# print(breadthFirstValues(a))
# #    -> ['a', 'b', 'c', 'x', 'd', 'e']
# # test_04:
# print(breadthFirstValues(null))
# #    -> []
