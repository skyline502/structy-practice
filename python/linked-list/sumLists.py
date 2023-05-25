# sum list

# Write a function, sumList,
# that takes in the head of a
# linked list containing numbers
# as an argument. The function
# should return the total sum of
# all values in the linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sumList(head):
  sum = 0

  while head:
    sum += head.val
    head = head.next

  return sum

# Examples:

# test_00:

a = Node(2);
b = Node(8);
c = Node(3);
d = Node(-1);
e = Node(7);

a.next = b;
b.next = c;
c.next = d;
d.next = e;

# 2 -> 8 -> 3 -> -1 -> 7

print(sumList(a)); # 19

#test_01:

x = Node(38);
y = Node(4);

x.next = y;

# 38 -> 4

print(sumList(x)); # 42

#test_02:

z = Node(100);

# 100

print(sumList(z)); # 100

#test_03:

print(sumList(None)); # 0
