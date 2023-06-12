# tree levels

# Write a function, print(treeLevels,) that takes in the root of a binary tree.
# The function should return a 2-Dimensional array where each subarray represents
# a level of the tree.

class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

def treeLevels(root):
  if root == None:
    return []

  levels = []

  # [node, current level]
  queue = [[root, 0]]

  while len(queue) > 0:
    current = queue.pop(0)
    # print(current[1])
    # if current == None:
    #   break
    if len(levels) <= current[1]:
      levels.append([current[0].val])
    else:
      levels[current[1]].append(current[0].val)

    if current[0].left != None:
      # increment level
      level = current[1] + 1
      queue.append([current[0].left, level])

    if current[0].right != None:
      level = current[1] + 1
      queue.append([current[0].right, level])

  return levels


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

print(treeLevels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
# test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")

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

print(treeLevels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]
# test_02:
q = Node("q")
r = Node("r")
s = Node("s")
t = Node("t")
u = Node("u")
v = Node("v")

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

print(treeLevels(q)) #->
# [
#   ['q'],
#   ['r', 's'],
#   ['t'],
#   ['u'],
#   ['v']
# ]
# test_03:
print(treeLevels(None)) # -> []
