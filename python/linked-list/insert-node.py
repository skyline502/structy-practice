# insert node

# Write a function, insertNode, that takes in the head of a linked list, a value,
# and an index.

# The function should insert a node with the value into the list at the specified
# index. Consider the head of the linked list as index 0. The function should return
# the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than
# the length of the input list.

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



def insertNode(head, val, idx):
  n = Node(val)
  if idx == 0:
    n.next = head
    return linkedListValues(n)

  start = head
  i = 0


  while head:
    if i + 1 == idx:
      pnext = head.next
      head.next = n
      n.next = pnext
      return linkedListValues(start)

    head = head.next
    i += 1





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

print(insertNode(a, 'x', 2))
# a -> b -> x -> c -> d
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(insertNode(a, 'v', 3))
# a -> b -> c -> v -> d
# test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(insertNode(a, 'm', 4))
# a -> b -> c -> d -> m


# test_03:
# a = Node("a")
# b = Node("b")

a.next = b

# a -> b

print(insertNode(a, 'z', 0))
# z -> a -> b
