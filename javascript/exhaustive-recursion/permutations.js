/*
permutations
Write a function, permutations, that takes in an array an argument. The function should return a 2D array where each subarray represents one of the possible permutations of the array.

The subarrays may be returned in any order.

You may assume that the input array contains unique elements.

test_00:
permutations(['a', 'b', 'c']); // ->
// [
//   [ 'a', 'b', 'c' ],
//   [ 'b', 'a', 'c' ],
//   [ 'b', 'c', 'a' ],
//   [ 'a', 'c', 'b' ],
//   [ 'c', 'a', 'b' ],
//   [ 'c', 'b', 'a' ]
// ]
test_01:
permutations(['red', 'blue']); // ->
// [
//   [ 'red', 'blue' ],
//   [ 'blue', 'red' ]
// ]
test_02:
permutations([8, 2, 1, 4]); // ->
// [
//   [ 8, 2, 1, 4 ], [ 2, 8, 1, 4 ],
//   [ 2, 1, 8, 4 ], [ 2, 1, 4, 8 ],
//   [ 8, 1, 2, 4 ], [ 1, 8, 2, 4 ],
//   [ 1, 2, 8, 4 ], [ 1, 2, 4, 8 ],
//   [ 8, 1, 4, 2 ], [ 1, 8, 4, 2 ],
//   [ 1, 4, 8, 2 ], [ 1, 4, 2, 8 ],
//   [ 8, 2, 4, 1 ], [ 2, 8, 4, 1 ],
//   [ 2, 4, 8, 1 ], [ 2, 4, 1, 8 ],
//   [ 8, 4, 2, 1 ], [ 4, 8, 2, 1 ],
//   [ 4, 2, 8, 1 ], [ 4, 2, 1, 8 ],
//   [ 8, 4, 1, 2 ], [ 4, 8, 1, 2 ],
//   [ 4, 1, 8, 2 ], [ 4, 1, 2, 8 ]
// ]
test_03:
permutations([]); // ->
// [
//  [ ]
// ]
const permutations = (items) => {
  if (!items.length) return [[]];
  let first = items[0];
  let rest = permutations(items.slice(1));

  let permutation = []
  for (let item of rest) {
    for (let i = 0; i <= item.length; i++) {
      permutation.push([...item.slice(0, i), first, ...item.slice(i)])
    }
  }
  return permutation;
};
*/
