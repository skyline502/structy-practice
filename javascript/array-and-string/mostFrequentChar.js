/*
most frequent char
Write a function, mostFrequentChar, that takes in a string as
an argument. The function should return the most frequent character
of the string. If there are ties, return the character that appears
earlier in the string.

You can assume that the input string is non-empty.
*/

const mostFrequentChar = str => {
  const count = {};

  for (char of str) {
    if (!count[char]) {
      count[char] = 1;
    } else {
      count[char]++;
    }
  }

  // console.log(count, 'count')

  let max = 0;
  let letter;

  for (n in count) {
    if (count[n] > max) {
      max = count[n]
      letter = n;
    }
  }

  return letter;
}


// test_00:
console.log(mostFrequentChar('bookeeper')); // -> 'e'
// test_01:
console.log(mostFrequentChar('david')); // -> 'd'
// test_02:
console.log(mostFrequentChar('abby')); // -> 'b'
// test_03:
console.log(mostFrequentChar('mississippi')); // -> 'i'
// test_04:
console.log(mostFrequentChar('potato')); // -> 'o'
// test_05:
console.log(mostFrequentChar('eleventennine')); // -> 'e'
// test_06:
console.log(mostFrequentChar("riverbed")); // -> 'r'
