const anagrams = (s1, s2) => {
  if (s1.length !== s2.length) return false;
  let char = {}
  for (let i = 0; i < s1.length; i++) {
    let letter = s1[i];
    if (char[letter]) {
      char[letter] += 1;
    } else {
      char[letter] = 1;
    }
  }

  for (let c of s2) {
    if (!char[c]) {
      return false;
    }
    char[c] -= 1;
  }

  for (let count in char) {
    if (char[count] > 0) {
      return false;
    }
  }
  return true;
};
