# tree value count

# Write a function, treeValueCount, that takes in the root of a
# binary tree and a target value. The function should return the
# number of times that the target occurs in the tree.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def treeValueCount(root, tar):
  if root == None:
    return 0

  stack = [root]
  count = 0

  while len(stack) > 0:
    current = stack.pop()
    left = current.left
    right = current.right

    if left:
      stack.append(left)

    if right:
      stack.append(right)

    if current.val == tar:
      count += 1

  return count

# Examples:
a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

print(treeValueCount(a,  6)) # -> 3

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# #      12
# #    /   \
# #   6     6
# #  / \     \
# # 4  6     12

print(treeValueCount(a,  12)) # -> 2

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

# #      7
# #    /   \
# #   5     1
# #  / \     \
# # 1   8     7
# #    /       \
# #   1         1
print(treeValueCount(a, 1)) # -> 4

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

# #      7
# #    /   \
# #   5     1
# #  / \     \
# # 1   8     7
# #    /       \
# #   1         1

print(treeValueCount(a, 9)) # -> 0

print(treeValueCount(None, 42)) # -> 0
