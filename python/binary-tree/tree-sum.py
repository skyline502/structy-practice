# tree sum
#
# Write a function, treeSum, that takes in the root of a binary tree that contains number values.
# The function should return the total sum of all values in the tree.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def treeSum(root):
  if root == None:
    return 0
  sum = 0

  stack = [root]

  while len(stack) > 0:
    current = stack.pop()

    if current.left:
      stack.append(current.left)

    if current.right:
      stack.append(current.right)

    sum += current.val

  return sum

# Examples:

# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1

# print(treeSum(a)) # -> 21

# # test_01:
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

# #      1
# #    /   \
# #   6     0
# #  / \     \
# # 3   -6    2
# #    /       \
# #   2         2

print(treeSum(a)) # -> 10
# test_02:
print(treeSum(None)) # -> 0
