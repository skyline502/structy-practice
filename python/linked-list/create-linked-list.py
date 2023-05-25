# create linked list

# Write a function, createLinkedList, that takes in an array of values as an
# argument.

# The function should create a linked list containing each element of the array as
# the values of the nodes. The function should return the head of the linked list.

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


def createLinkedList(list):
  if len(list) < 1:
    return None

  head = None
  cur = None

  for el in list:
    if head == None:
      head = Node(el)
      cur = head
    else:
      n = Node(el)
      cur.next = n
      cur = n

  return linkedListValues(head)


# Examples:
# test_00:
print(createLinkedList(["h", "e", "y"]));
# h -> e -> y
# test_01:
print(createLinkedList([1, 7, 1, 8]));
# 1 -> 7 -> 1 -> 8
# test_02:
print(createLinkedList(["a"]));
# a
# test_03:
print(createLinkedList([]));
# null
