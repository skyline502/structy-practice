# tree includes

# Write a function, treeIncludes, that takes in the root of a binary tree and a target value.
# The function should return a boolean indicating whether or not the value is contained in the tree.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def treeIncludes(root, target):
  if root == None:
    return False

  queue = [root]

  while len(queue) > 0:
    current = queue.pop(0)

    if current.val == target:
      return True

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)

  return False

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

print(treeIncludes(a, "e")) # -> true
# # test_01:
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

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

print(treeIncludes(a, "a")) # -> true
# # test_02:
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

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

print(treeIncludes(a, "n")) # -> false
# # test_03:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

print(treeIncludes(a, "f")) # -> true
# # test_04:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

print(treeIncludes(a, "p")) # -> false
# # test_05:
print(treeIncludes(None, "b")) # -> false
