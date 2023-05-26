# linked list find

# Write a function, linkedListFind, that takes in the head of a
# linked list and a target value. The function should return a
# boolean indicating whether or not the linked list contains the target.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linkedListFind(head, tar):

  while head:
    if head.val == tar:
      return True
    head = head.next

  return False

# Examples:
# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linkedListFind(a, "c")) # true
# test_01:

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linkedListFind(a, "d")) # true
# test_02:

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linkedListFind(a, "q")) # false
# test_03:
node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

print(linkedListFind(node1, "jason")) # true
# test_04:
node1 = Node(42)

# 42

print(linkedListFind(node1, 42)) # true
# test_05:
node2 = Node(42)

# 42

print(linkedListFind(node1, 100)) # false
