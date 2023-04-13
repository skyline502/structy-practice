/*

breadth first values
Write a function, breadthFirstValues, that takes in the root of a binary tree.
The function should return an array containing all values of the tree in breadth-first
order.

*/

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const breadthFirstValues = root => {
  if (!root) {
    return [];
  }

  let queue = [root];
  let values = [];

  while (queue.length) {
    let current = queue.shift();
    // console.log(current)
    values.push(current.val);

    if (current.left) {
      queue.push(current.left);
    }

    if (current.right) {
      queue.push(current.right);
    }
  }

  return values;
}


// test_00:
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

console.log(breadthFirstValues(a));
//    -> ['a', 'b', 'c', 'd', 'e', 'f']
// // test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f
// //    /       \
// //   g         h

// console.log(breadthFirstValues(a));
//   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
// test_02:
// const a = new Node('a');

// //      a

// console.log(breadthFirstValues(a));
// //    -> ['a']
// // test_03:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const x = new Node('x');

// a.right = b;
// b.left = c;
// c.left = x;
// c.right = d;
// d.right = e;

// //      a
// //       \
// //        b
// //       /
// //      c
// //    /  \
// //   x    d
// //         \
// //          e

// console.log(breadthFirstValues(a));
// //    -> ['a', 'b', 'c', 'x', 'd', 'e']
// // test_04:
// console.log(breadthFirstValues(null));
// //    -> []
