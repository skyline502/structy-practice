# merge lists

# Write a function, mergeLists, that takes in the head of
# sorted linked lists as arguments.
# The function should merge the two lists together into
# single sorted linked list.
# The function should return the head of the merged linked
# list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and
# contain increasing sorted numbers.

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


def mergeLists(h1, h2):
    cur = None
    nex = None
    head = None

    if h1.val < h2.val:
        cur = h1
        nex = h2
        head = cur
    else:
        cur = h2
        nex = h1
        head = cur

    while cur:
        curNext = cur.next
        if curNext.val < nex.val:
            cur = cur.next
        else:
            cur.next = nex
            cur = nex
            nex = curNext

    return linkedListValues(head)




# Examples:

# # test_00:
a = Node(5);
b = Node(7);
c = Node(10);
d = Node(12);
e = Node(20);
f = Node(28);
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6);
r = Node(8);
s = Node(9);
t = Node(25);
q.next = r;
r.next = s;
s.next = t;
# 6 -> 8 -> 9 -> 25

print(mergeLists(a, q));
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
# test_01:
a = Node(5);
b = Node(7);
c = Node(10);
d = Node(12);
e = Node(20);
f = Node(28);
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(1);
r = Node(8);
s = Node(9);
t = Node(10);
q.next = r;
r.next = s;
s.next = t;
# 1 -> 8 -> 9 -> 10

print(mergeLists(a, q));
# # 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28
# # test_02:
# h = Node(30);
# # 30

# p = Node(15);
# q = Node(67);
# p.next = q;
# # 15 -> 67

# mergeLists(h, p);
# # 15 -> 30 -> 67
