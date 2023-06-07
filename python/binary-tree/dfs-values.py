# depth first values

# Write a function, df_values, that takes in the root
# of a binary tree. The function should return an array containing
# all values of the tree in depth-first order.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def df_values(root):
  values = []
  stack = [root]

  while len(stack) > 0:
    current = stack.pop()
    if current == None:
      return values
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
    values.append(current.val)

  return values


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

print(df_values(a));
#    -> ['a', 'b', 'd', 'e', 'c', 'f']
# test_01:
a = Node('a');
b = Node('b');
c = Node('c');
d = Node('d');
e = Node('e');
f = Node('f');
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

print(df_values(a));
#    -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# test_02:
o = Node('a');
#      a
print(df_values(o));
#    -> ['a']
# test_03:
j = Node('a');
k = Node('b');
l = Node('c');
m = Node('d');
n = Node('e');

j.right = k;
k.left = l;
l.right = m;
m.right = n;

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

print(df_values(j));
#    -> ['a', 'b', 'c', 'd', 'e']
# test_04:
print(df_values(None));
#    -> []
