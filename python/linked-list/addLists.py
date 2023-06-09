# add lists

# Write a function, addLists, that takes in the head of two linked lists, each representing a
# number.

# The nodes of the linked lists contain digits as values. The nodes in the input lists are
# reversed;

# This means that the least significant digit of the number is the head. The function should
# return the head of a linked listed representing the sum of the input lists. The output list
# should have its digits reversed as well.

# Say we wanted to compute 621 + 354 normally. The sum is 975:

#    621
#  + 354
#  -----
#    975

# Then, the reversed linked list format of this problem would appear as:

#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9

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


def addLists(h1, h2):
    h1nums = []
    h2nums = []

    while (h1):
        h1nums.append(str(h1.val))
        h1 = h1.next

    while (h2):
        h2nums.append(str(h2.val))
        h2 = h2.next

    print(h1nums, h2nums, 'before')
    h1nums.reverse()
    h2nums.reverse()
    print(h1nums, h2nums, 'after')


    result = (str(int("".join(h1nums)) + int("".join(h2nums))))

    res = result[::-1]

    head = None
    current = None
    for char in res:
        c = Node(int(char))
        if head == None:
            head = c
            current = c
        current.next = c
        current = c

    return linkedListValues(head)




# Examples:

# a1 = Node(1);
# a2 = Node(2);
# a3 = Node(6);
# a1.next = a2;
# a2.next = a3;
# # 1 -> 2 -> 6

# b1 = Node(4);
# b2 = Node(5);
# b3 = Node(3);
# b1.next = b2;
# b2.next = b3;
# # 4 -> 5 -> 3

# print(addLists(a1, b1));
# 5 -> 7 -> 9


# test_01:
#  7541
# +  32
# -----
#  7573

a1 = Node(1);
a2 = Node(4);
a3 = Node(5);
a4 = Node(7);
a1.next = a2;
a2.next = a3;
a3.next = a4;
# # 1 -> 4 -> 5 -> 7

b1 = Node(2);
b2 = Node(3);
b1.next = b2;
# # 2 -> 3

print(addLists(a1, b1))
# # 3 -> 7 -> 5 -> 7

# # test_02:
# #   39
# # + 47
# # ----
# #   86

# a1 = Node(9);
# a2 = Node(3);
# a1.next = a2;
# # 9 -> 3

# b1 = Node(7);
# b2 = Node(4);
# b1.next = b2;
# # 7 -> 4

# addLists(a1, b1);
# # 6 -> 8
# # test_03:
# #   89
# # + 47
# # ----
# #  136

# a1 = Node(9);
# a2 = Node(8);
# a1.next = a2;
# # 9 -> 8

# b1 = Node(7);
# b2 = Node(4);
# b1.next = b2;
# # 7 -> 4

# addLists(a1, b1);
# # 6 -> 3 -> 1
# # test_04:
# #   999
# #  +  6
# #  ----
# #  1005

# a1 = Node(9);
# a2 = Node(9);
# a3 = Node(9);
# a1.next = a2;
# a2.next = a3;
# # 9 -> 9 -> 9

# b1 = Node(6);
# # 6

# addLists(a1, b1);
# # 5 -> 0 -> 0 -> 1
