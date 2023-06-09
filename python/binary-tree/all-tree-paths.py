# all tree paths

# Write a function, print(allTreePaths,) that takes in the root of a binary tree. The function should return a 2-Dimensional array where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer array does not matter.

# You may assume that the input tree is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def allTreePaths(root):
  if root == None:
    return []

  if root.left == None and root.right == None:
    return [[root.val]]

  paths = []
  left_path = allTreePaths(root.left)

  for path in left_path:
    paths.append([root.val, *path])

  right_path = allTreePaths(root.right)

  for path in right_path:
    paths.append([root.val, *path])

  return paths



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

print(allTreePaths(a)) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]

# test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i

print(allTreePaths(a)) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e', 'g' ],
#   [ 'a', 'b', 'e', 'h' ],
#   [ 'a', 'c', 'f', 'i' ]
# ]

# test_02:
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')

q.left = r
q.right = s
r.right = t
t.left = u
u.right = v

#      q
#    /   \
#   r     s
#    \
#     t
#    /
#   u
#  /
# v

print(allTreePaths(q)) # ->
# [
#   [ 'q', 'r', 't', 'u', 'v' ],
#   [ 'q', 's' ]
# ]

# test_03:
z = Node('z')

#      z

print(allTreePaths(z)) # ->
# [
#   ['z']
# ]
