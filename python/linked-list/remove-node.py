# remove node

# Write a function, removeNode, that takes in the head of a linked list and a
# target value as arguments.
# The function should delete the node containing the target value from the linked list
# and return the head of the resulting linked list. If the target appears multiple times
# in the linked list, only remove the first instance of the target in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def removeNode(head, tar):
  print(head.val, tar)


# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(removeNode(a, "c"))
# a -> b -> d -> e -> f
# test_01:
x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z

# x -> y -> z

print(removeNode(x, "z"))
# x -> y
# test_02:
q = Node("q")
r = Node("r")
s = Node("s")

q.next = r
r.next = s

# q -> r -> s

print(removeNode(q, "q"))
# r -> s
# test_03:
node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")

node1.next = node2
node2.next = node3
node3.next = node4

# h -> i -> j -> i

print(removeNode(node1, "i"))
# h -> j -> i
# test_04:
t = Node("t")

# t

print(removeNode(t, "t"))
# None
