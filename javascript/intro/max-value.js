//Max Value
/*
max value
Write a function, maxValue, that takes in array of numbers as an argument. The function should return the largest number in the array.

Solve this without using any built-in array methods.

You can assume that the array is non-empty.

// test_00:
console.log(maxValue([4, 7, 2, 8, 10, 9]); // -> 10
// test_01:
console.log(maxValue([10, 5, 40, 40.3]); // -> 40.3
// test_02:
console.log(maxValue([-5, -2, -1, -11]); // -> -1
// test_03:
console.log(maxValue([42]); // -> 42
// test_04:
console.log(maxValue([1000, 8]); // -> 1000
// test_05:
console.log(maxValue([1000, 8, 9000]); // -> 9000
// test_06:
console.log(maxValue([2, 5, 1, 1, 4]); // -> 5
*/

const maxValue = arr => {
  let max = -Infinity;

  for (let val of arr) {
    if (val > max) {
      max = val;
    }
  }

  return max;
}

// test_00:
console.log(maxValue([4, 7, 2, 8, 10, 9])); // -> 10
// test_01:
console.log(maxValue([10, 5, 40, 40.3])); // -> 40.3
// test_02:
console.log(maxValue([-5, -2, -1, -11])); // -> -1
// test_03:
console.log(maxValue([42])); // -> 42
// test_04:
console.log(maxValue([1000, 8])); // -> 1000
// test_05:
console.log(maxValue([1000, 8, 9000])); // -> 9000
// test_06:
console.log(maxValue([2, 5, 1, 1, 4])); // -> 5
