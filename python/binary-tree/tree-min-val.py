# tree min value

# Write a function, treeMinValue, that takes in the root of a binary
# tree that contains number values. The function should return the
# minimum value within the tree.

# You may assume that the input tree is non-empty.


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def treeMinValue(root):
  min_val = float('inf')
  stack = [root]

  while len(stack) > 0:
    current = stack.pop()

    if current.val < min_val:
      min_val = current.val

    if current.right:
      stack.append(current.right)

    if current.left:
      stack.append(current.left)

  return min_val


# test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(treeMinValue(a)) # -> -2
# test_01:
a = Node(5);
b = Node(11);
c = Node(3);
d = Node(4);
e = Node(14);
f = Node(12);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

# #       5
# #    /    \
# #   11     3
# #  / \      \
# # 4   14     12

print(treeMinValue(a)); # -> 3
# # test_02:
a = Node(-1);
b = Node(-6);
c = Node(-5);
d = Node(-3);
e = Node(-4);
f = Node(-13);
g = Node(-2);
h = Node(-2);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;
f.right = h;

# #        -1
# #      /   \
# #    -6    -5
# #   /  \     \
# # -3   -4   -13
# #     /       \
# #    -2       -2

print(treeMinValue(a)); # -> -13
# # test_03:
# a = Node(42);

# #        42

# print(treeMinValue(a)); # -> 42
