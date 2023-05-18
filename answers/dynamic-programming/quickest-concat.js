const quickestConcat = (s, words) => {
  let result = _quickestConcat(s, words);
  if (result === Infinity) {
    return -1;
  } else {
    return result;
  }
};

const _quickestConcat = (s, words, memo = {}) => {
  if (s in memo) return memo[s];
  if (!s.length) return 0;
  let min = Infinity;

  for (let word of words) {
    if (s.startsWith(word)) {
      let rest = s.slice(word.length);
      let result = 1 + _quickestConcat(rest, words, memo);
      min = Math.min(min, result);
    }
  }

  memo[s] = min;
  return min;
}
