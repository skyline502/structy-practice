# how high

# Write a function, print(howHigh,) that takes in the root of a binary tree.
# The function should return a number representing the height of the tree.

# The height of a binary tree is defined as the maximal number of edges
# from the root node to any leaf node.

# If the tree is empty, return -1.

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

def howHigh(root):
  if root == None:
    return -1

  height = 0
  stack = [[root, 0]]

  while len(stack) > 0:
    current = stack.pop()

    node = current[0]
    level = current[1]

    # print(node.val, level)
    # print('current height', height, 'current level:', level)

    if level > height:
      # print('does it reach here...', node.val, level)
      height = level

    if node.left:
      stack.append([node.left, level + 1])

    if node.right:
      stack.append([node.right, level + 1])

  return height

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

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

print(howHigh(a)) # -> 2
# test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(howHigh(a)) # -> 3
# test_02:
a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

print(howHigh(a)) # -> 1
# test_03:
a = Node('a')

#      a

print(howHigh(a)) # -> 0
# test_04:
print(howHigh(None)) # -> -1
