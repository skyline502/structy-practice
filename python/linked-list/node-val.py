# get node value

# Write a function, getNodeValue, that takes in the head
# of a linked list and an index. The function should
# return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

def getNodeValue(head, i):
  idx = 0

  while head:
    if idx == i:
      return head.val
    head = head.next
    idx += 1

  return None

# Examples:
# test_00:
a = Node("a");
b = Node("b");
c = Node("c");
d = Node("d");

a.next = b;
b.next = c;
c.next = d;

# a -> b -> c -> d

print(getNodeValue(a, 2))# 'c'
# test_01:
# a = Node("a");
# b = Node("b");
# c = Node("c");
# d = Node("d");

a.next = b;
b.next = c;
c.next = d;

# a -> b -> c -> d

print(getNodeValue(a, 3))# 'd'
# test_02:
# a = Node("a");
# b = Node("b");
# c = Node("c");
# d = Node("d");

a.next = b;
b.next = c;
c.next = d;

# a -> b -> c -> d

print(getNodeValue(a, 7))# None
# test_03:
node1 = Node("banana");
node2 = Node("mango");

node1.next = node2;

# banana -> mango

print(getNodeValue(node1, 0))# 'banana'
# test_04:
# node1 = Node("banana");
# node2 = Node("mango");

node1.next = node2;

# banana -> mango

print(getNodeValue(node1, 1))# 'mango'
