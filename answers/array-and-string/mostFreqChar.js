const mostFrequentChar = (s) => {
  let count = {};
  let letter;
  let max = 0;
  for (let char of s) {
    if (!count[char]) {
      count[char] = 1;
    } else {
      count[char]++;
    }
  }

  for (let char in count) {
    if (count[char] > max) {
      max = count[char];
      letter = char
    }
  }

  return letter;


};
