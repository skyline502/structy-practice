# linked list values

# Write a function, linkedListValues, that takes in the
# head of a linked list as an argument. The function
# should return an array containing all values of the
# nodes in the linked list.

# Examples:

a = new Node("a");
b = new Node("b");
c = new Node("c");
d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

#a -> b -> c -> d

print(linkedListValues(a)); #-> [ 'a', 'b', 'c', 'd' ]
x = new Node("x");
y = new Node("y");

x.next = y;

#x -> y

print(linkedListValues(x)); #-> [ 'x', 'y' ]
q = new Node("q");

#q

print(linkedListValues(q)); #-> [ 'q' ]
print(linkedListValues(null)); #-> [ ]
