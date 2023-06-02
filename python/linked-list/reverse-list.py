# reverse list

# Write a function, reverseList, that takes in the head of a
# linked list as an argument. The function should reverse the
# order of the nodes in the linked list in-place and return
# the head of the reversed linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linkedListValues(head):
   result = []

   while head:
      result.append(head.val)
      head = head.next

   return result

def reverseList(head):
  print(head)

# Examples:
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

print(reverseList(a)) # f -> e -> d -> c -> b -> a
# test_01:
x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(reverseList(x)) # y -> x
# test_02:
p = Node("p")

# p

print(reverseList(p)) # p
