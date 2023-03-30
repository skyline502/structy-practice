/*
linked list find

Write a function, linkedListFind, that takes in the head of a
linked list and a target value. The function should return a
boolean indicating whether or not the linked list contains the target.


*/

const linkedListFind = (head, tar) => {
  if (head === null) return false;
  if (head.val === tar) return true;
  return linkedListFind(head.next, tar);
}

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

// test_00:
const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(linkedListFind(a, "c")); // true
// test_01:

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(linkedListFind(a, "d")); // true
// test_02:

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(linkedListFind(a, "q")); // false
// test_03:
let node1 = new Node("jason");
const node2 = new Node("leneli");

node1.next = node2;

// jason -> leneli

console.log(linkedListFind(node1, "jason")); // true
// test_04:
node1 = new Node(42);

// 42

console.log(linkedListFind(node1, 42)); // true
// test_05:
// const node2 = new Node(42);

// 42

console.log(linkedListFind(node1, 100)); // false
