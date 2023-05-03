/*
how high
Write a function, howHigh, that takes in the root of a binary tree.
The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges
from the root node to any leaf node.

If the tree is empty, return -1.

test_00:
const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

howHigh(a); // -> 2
test_01:
const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');
const g = new Node('g');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /
//   g

howHigh(a); // -> 3
test_02:
const a = new Node('a');
const c = new Node('c');

a.right = c;

//      a
//       \
//        c

howHigh(a); // -> 1
test_03:
const a = new Node('a');

//      a

howHigh(a); // -> 0
test_04:
howHigh(null); // -> -1
*/

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const howHigh = root => {
  if (!root) return -1;
  let left = howHigh(root?.left) || 0
  let right = howHigh(root?.right) || 0

  return 1 + Math.max(left, right);

}

//Examples:

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

console.log(howHigh(a)); // -> 2
console.log(howHigh(null)); // -> -1

const g = new Node('g');
e.left = g

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /
//   g

console.log(howHigh(a)); // -> 3

const h = new Node('h');
const i = new Node('i');

h.right = i;

//      a
//       \
//        c

console.log(howHigh(h)); // -> 1

const j = new Node('j');
console.log(howHigh(j)) // -> 0
