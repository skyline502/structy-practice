# longest streak

# Write a function, longestStreak, that takes in the head of a
# linked list as an argument. The function should return the
# length of the longest consecutive streak of the same value
# within the list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def longestStreak(head):
    if head == None:
        return 0

    longest = 0
    current = 0
    el = head.val

    while head:
        if head.val == el:
            current += 1
            if current > longest:
              longest = current
        else:
            el = head.val
            current = 1
        head = head.next

    return longest



# Examples:

# test_00:
a = Node(5);
b = Node(5);
c = Node(7);
d = Node(7);
e = Node(7);
f = Node(6);

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longestStreak(a)); # 3
# test_01:
a = Node(3);
b = Node(3);
c = Node(3);
d = Node(3);
e = Node(9);
f = Node(9);

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

# 3 -> 3 -> 3 -> 3 -> 9 -> 9

print(longestStreak(a)); # 4
# test_02:
a = Node(9);
b = Node(9);
c = Node(1);
d = Node(9);
e = Node(9);
f = Node(9);

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

print(longestStreak(a)); # 3
# test_03:
a = Node(5);
b = Node(5);

a.next = b;

# 5 -> 5

print(longestStreak(a)); # 2
# test_04:
a = Node(4);

# 4

print(longestStreak(a)); # 1
# test_05:
print(longestStreak(None)); # 0
