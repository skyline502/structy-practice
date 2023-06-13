/*
level averages

Write a function, levelAverages, that takes in the root of a binary tree that
contains number values. The function should return an array containing the average
value of each level.

*/

class Node {
  constructor(val) {
    this.val = val
    this.left = null
    this.right = null
  }
}


const levelAverages = root => {
  let levels = []
  let queue = [[root, 0]]

  while (queue.length) {
    let current = queue.shift()
    let node = current[0]
    let level = current[1]

    if (levels.length <= level) {
      levels.push([node.val])
    } else {
      levels[level].push(node.val)
    }

    if (node.left) {
      queue.push([node.left, level + 1])
    }

    if (node.right) {
      queue.push([node.right, level + 1])
    }
  }

  let levelavg = []

  for (let arr of levels) {
    let length = arr.length
    let sum = 0

    for (let num of arr) {
      sum += num
    }

    levelavg.push(sum/length)
  }

  return levelavg;
}



// test_00:
const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
const d = new Node(4);
const e = new Node(-2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1

console.log(levelAverages(a)); // -> [ 3, 7.5, 1 ]
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;

// //        5
// //     /    \
// //    11    54
// //  /   \
// // 20   15
// //      / \
// //     1  3

// levelAverages(a); // -> [ 5, 32.5, 17.5, 2 ]
// // test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(0);
// const f = new Node(45);
// const g = new Node(-1);
// const h = new Node(-2);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //        -1
// //      /   \
// //    -6    -5
// //   /  \     \
// // -3   0     45
// //     /       \
// //    -1       -2

// levelAverages(a); // -> [ -1, -5.5, 14, -1.5 ]
// // test_03:
// const q = new Node(13);
// const r = new Node(4);
// const s = new Node(2);
// const t = new Node(9);
// const u = new Node(2);
// const v = new Node(42);

// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;

// //        13
// //      /   \
// //     4     2
// //      \
// //       9
// //      /
// //     2
// //    /
// //   42

// levelAverages(q); // -> [ 13, 3, 9, 2, 42 ]
// // test_04:
// levelAverages(null); // -> [ ]
