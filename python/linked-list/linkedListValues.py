# linked list values

# Write a function, linkedListValues, that takes in the
# head of a linked list as an argument. The function
# should return an array containing all values of the
# nodes in the linked list.

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

# Examples:

a = Node("a");
b = Node("b");
c = Node("c");
d = Node("d");

a.next = b;
b.next = c;
c.next = d;

#a -> b -> c -> d

print(linkedListValues(a)); #-> [ 'a', 'b', 'c', 'd' ]
x = Node("x");
y = Node("y");

x.next = y;

#x -> y

print(linkedListValues(x)); #-> [ 'x', 'y' ]
q = Node("q");

#q

print(linkedListValues(q)); #-> [ 'q' ]
print(linkedListValues(None)); #-> [ ]
