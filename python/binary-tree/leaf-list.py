# leaf list

# Write a function, print(leafList,) that takes in the root of a binary tree and
# returns an array containing the values of all leaf nodes in left-to-right order.

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

print(leafList(a)) # -> [ 'd', 'e', 'f' ]
# test_01:
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

print(leafList(a)) # -> [ 'd', 'g', 'h' ]
# test_02:
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

print(leafList(a)) # -> [ 20, 1, 3, 54 ]
# test_03:
x = Node('x')

#      x

print(leafList(x)) # -> [ 'x' ]
# test_04:
print(leafList(None)) # -> [ ]
