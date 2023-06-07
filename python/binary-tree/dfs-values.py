# depth first values

# Write a function, depthFirstValues, that takes in the root
# of a binary tree. The function should return an array containing
# all values of the tree in depth-first order.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def df_values(root):
  print(root)


# Examples:

# test_00:
a = Node('a');
b = Node('b');
c = Node('c');
d = Node('d');
e = Node('e');
f = Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(depthFirstValues(a));
#    -> ['a', 'b', 'd', 'e', 'c', 'f']
# test_01:
# a = Node('a');
# b = Node('b');
# c = Node('c');
# d = Node('d');
# e = Node('e');
# f = Node('f');
g = Node('g');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(depthFirstValues(a));
#    -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# test_02:
# a = Node('a');
#      a
print(depthFirstValues(a));
#    -> ['a']
# test_03:
# a = Node('a');
# b = Node('b');
# c = Node('c');
# d = Node('d');
# e = Node('e');

a.right = b;
b.left = c;
c.right = d;
d.right = e;

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

print(depthFirstValues(a));
#    -> ['a', 'b', 'c', 'd', 'e']
# test_04:
print(depthFirstValues(None));
#    -> []
