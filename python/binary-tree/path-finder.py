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

# def pathFinder(root, target):
#   if root == None:
#     return None

#   if root.val == target:
#     return [root.val]

#   left = pathFinder(root.left, target)
#   right = pathFinder(root.right, target)

#   if left != None:
#     return [root.val, *left]

#   if right != None:
#     return [root.val, *right]

#   return None

def pathFinder(root, target):
  results = findVal(root, target)

  # print(results, 'results')

  if results != None:
    print('results found')
    results.reverse()
    return results
  else:
    return None

def findVal(root, tar):
  if root == None:
     return None
  # print(root.val, tar, 'line 43')

  if root.val == tar:
     return [root.val] #we return an array when we find the target;

  left = findVal(root.left, tar) #else we continue down the nodes in search of it
  right = findVal(root.right, tar)

  # print(left, right)

  if left != None: #if it is found on the left node, we push the root val into our array
    left.append(root.val)
    return left

  if right != None: #if it is on the right, we do the same;
    right.append(root.val)
    return right

  return None #finally if the tar is not found we return null;



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

print(pathFinder(a, 'p')) # -> None
# # test_02:
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

print(pathFinder(a, "c")) # -> ['a', 'c']
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

print(pathFinder(a, "h")) # -> ['a', 'c', 'f', 'h']
# test_04:
x = Node("x")

#      x

print(pathFinder(x, "x")) # -> ['x']
# test_05:
print(pathFinder(None, "x")) # -> None
# test_06:
root = Node(0)
curr = root
for i in range(6000):
  curr.right = Node(i)
  curr = curr.right


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

print(pathFinder(root, 3451)) # -> [0, 1, 2, 3, ..., 3450, 3451]
