/*
five sort
Write a function, fiveSort, that takes in an array of numbers as an argument.
The function should rearrange elements of the array such that all 5s appear
at the end. Your function should perform this operation in-place by mutating
the original array. The function should return the array.

Elements that are not 5 can appear in any order in the output,
as long as all 5s are at the end of the array.
*/

const fiveSort = nums => {
  let first = 0;
  let last = nums.length - 1;

  while (first < last) {
    if (nums[last] === 5) { //if last number is a 5, decrement index
      last--;
    } else if (nums[first] === 5) { //else if first num ===5 move to end;
      [nums[first], nums[last]] = [nums[last], nums[first]];
      first++;
    } else {
      first++;
    }
  }

  return nums;
}

// test_00
console.log(fiveSort([12, 5, 1, 5, 12, 7]));
// -> [12, 7, 1, 12, 5, 5]
// test_01
console.log(fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]));
// -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
// test_02
console.log(fiveSort([5, 5, 5, 1, 1, 1, 4]));
// -> [4, 1, 1, 1, 5, 5, 5]
// test_03
console.log(fiveSort([5, 5, 6, 5, 5, 5, 5]));
// -> [6, 5, 5, 5, 5, 5, 5]
// test_04
console.log(fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]));
// -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
// test_05
const fives = new Array(20000).fill(5);
const fours = new Array(20000).fill(4);
const nums = [...fives, ...fours];
console.log(fiveSort(nums));
// twenty-thousand 4s followed by twenty-thousand 5s
// -> [4, 4, 4, 4, ..., 5, 5, 5, 5]
