/*

reverse list

Write a function, reverseList, that takes in the head of a
linked list as an argument. The function should reverse the
order of the nodes in the linked list in-place and return
the new head of the reversed linked list.

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

const reverseList = (head) => {
  let prev = null;

  while (head) {
    let next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }

  let nodes = linkedListValues(prev);
  console.log(nodes, 'nodes....')
  return prev;
}

// test_00:
const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

// a -> b -> c -> d -> e -> f

console.log(reverseList(a)); // f -> e -> d -> c -> b -> a
// test_01:
const x = new Node("x");
const y = new Node("y");

x.next = y;

// x -> y

console.log(reverseList(x)); // y -> x
// test_02:
const p = new Node("p");

// p

console.log(reverseList(p)); // p
