/*

insert node
Write a function, insertNode, that takes in the head of a linked list, a value, and an index.
The function should insert a new node with the value into the list at the specified index.
Consider the head of the linked list as index 0. The function should return the head of the
resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the
length of the input list.


*/

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const linkedListValues = head => {
  if (!head) {
    return [];
  }

  let results = [];

  while (head) {
    results.push(head.val);
    head = head.next;
  }

  return results;
}

const insertNode = (head, val, idx) => {
  let i = 0;
  let newNode = new Node(val);
  let start = head;

  if (idx === 0) {
    newNode.next = head;
    return linkedListValues(newNode);
  }

  while (head) {
    let next = head.next;
    if (idx === i + 1) {
      head.next = newNode;
      newNode.next = next;
      return linkedListValues(start);
    }
    head = head.next;
    i++;
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

console.log(insertNode(a, 'x', 2));
// a -> b -> x -> c -> d
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(insertNode(a, 'v', 3));
// a -> b -> c -> v -> d
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(insertNode(a, 'm', 4));
// a -> b -> c -> d -> m
// test_03:
// const a = new Node("a");
// const b = new Node("b");

a.next = b;

// a -> b

console.log(insertNode(a, 'z', 0));
// z -> a -> b
