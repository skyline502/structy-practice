# is univalue list

# Write a function, isUnivalueList, that takes in
# he head of a linked list as an argument.
# The function should return a boolean indicating
# whether or not the linked list contains exactly
# one unique value.

# You may assume that the input list is non-empty.

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

def isUnivalueList(head):
  current = head.val

  while head:
    if head.val != current:
      return False
    head = head.next

  return True

# Examples:

# test_00:
a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

print(isUnivalueList(a)) # true
# # test_01:
# a = Node(7)
# b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

print(isUnivalueList(a)) # false

# # test_02:
u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# # 2 -> 2 -> 2 -> 2 -> 2

print(isUnivalueList(u)) # true
# # test_03:
u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# # 2 -> 2 -> 3 -> 3 -> 2

print(isUnivalueList(u)) # false
# # test_04:
z = Node('z')

# z

print(isUnivalueList(z)) # true
