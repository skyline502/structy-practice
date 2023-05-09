/*
nesting score
Write a function, nestingScore, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
You may assume that the input only contains well-formed square brackets.

test_00:
nestingScore("[]"); // -> 1
test_01:
nestingScore("[][][]"); // -> 3
test_02:
nestingScore("[[]]"); // -> 2
test_03:
nestingScore("[[][]]"); // -> 4
test_04:
nestingScore("[[][][]]"); // -> 6
test_05:
nestingScore("[[][]][]"); // -> 5
test_06:
nestingScore("[][[][]][[]]"); // -> 7
test_07:
nestingScore("[[[[[[[][]]]]]]][]"); // -> 129
*/

// const nestingScore = (str) => {
  //[] = 1 pt
  //[[]] = 2 * [[val]] //here val is 1, so 2 * 1 = 2
  //[[][]] = 2 * [[val][val]], here we have 2 val's so 2 * 2 = 4
  //use stack?
//   let stack = [0];
//   for (let char of str) {
//       if (char === '[') {
//           stack.push(0);
//       } else {
//         const popped = stack.pop();
//         if (popped === 0) {
//           stack[stack.length - 1] += 1;
//         } else {
//           stack[stack.length - 1] += 2 * popped;
//         }
//       }
//   }
//   return stack[stack.length - 1];
// }
