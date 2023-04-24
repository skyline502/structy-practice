/*

tree path finder
Write a function, pathFinder, that takes in the root of a
binary tree and a target value. The function should return
an array representing a path to the target value. If the target
value is not found in the tree, then return null.

You may assume that the tree contains unique values.

*/

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const pathFinder = (root, tar) => {
  let results = findVal(root, tar);

  if (!results) {
    return null;
  } else {
    return results.reverse();
  }
}

const findVal = (root, tar) => {
  if (!root) return null;
  if (root.val === tar) return [root.val];
  let left = findVal(root.left, tar);
  let right = findVal(root.right, tar);

  if (left) {
    left.push(root.val);
    return left;
  }
  if (right) {
    right.push(root.val);
    return right;
  }
  return null;
}


// test_00:
const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

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

console.log(pathFinder(a, 'e')); // -> [ 'a', 'b', 'e' ]
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f

// console.log(pathFinder(a, 'p')); // -> null
// // test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");

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

// console.log(pathFinder(a, "c")); // -> ['a', 'c']
// // test_03:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");

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

// console.log(pathFinder(a, "h")); // -> ['a', 'c', 'f', 'h']
// test_04:
const x = new Node("x");

//      x

console.log(pathFinder(x, "x")); // -> ['x']
// test_05:
console.log(pathFinder(null, "x")); // -> null
// test_06:
const root = new Node(0);
let curr = root;
for (let i = 1; i <= 6000; i += 1) {
  curr.right = new Node(i);
  curr = curr.right;
}

//      0
//       \
//        1
//         \
//          2
//           \
//            3
//             .
//              .
//               .
//              5999
//                \
//                6000

console.log(pathFinder(root, 3451)); // -> [0, 1, 2, 3, ..., 3450, 3451]
