/*

anagrams

Write a function, anagrams, that takes in
two strings as arguments. The function should
return a boolean indicating whether or not the
strings are anagrams. Anagrams are strings that
contain the same characters, but in any order.


*/

const anagrams = (str1, str2) => {
  if (str1.length !== str2.length) {
    return false;
  }

  const count = {};

  for (char of str1) {
    if (char in count) {
      count[char]++;
    } else {
      count[char] = 1;
    }
  }

  for (char of str2) {
    if (!char in count) {
      return false;
    }

    count[char]--;
  }

  for (n in count) {
    if (count[n] !== 0) {
      return false;
    }
  }

  return true;
}

//test_00:

console.log(anagrams('restful', 'fluster')); // -> true
//test_01:

console.log(anagrams('cats', 'tocs')); // -> false
//test_02:

console.log(anagrams('monkeyswrite', 'newyorktimes')); // -> true
//test_03:

console.log(anagrams('paper', 'reapa')); // -> false
//test_04:

console.log(anagrams('elbow', 'below')); // -> true
//test_05:

console.log(anagrams('tax', 'taxi')); // -> false
//test_06:

console.log(anagrams('taxi', 'tax')); // -> false
//test_07:

console.log(anagrams('night', 'thing')); // -> true
//test_08:

console.log(anagrams('abbc', 'aabc')); // -> false
//test_09:

console.log(anagrams('po', 'popp')); // -> false
//test_10:

console.log(anagrams('pp', 'oo')) // -> false
