const compress = (s) => {
  let result = '';
  let count = 1;
  let index = 0;
  while (index < s.length) {
    let char = s[index];
    let next = s[index + 1];
    if (char === next) {
      count++;
      index++;
    } else {
      if (count === 1 ) {
        result += char;
      } else {
        result += count + char;
      }
      count = 1;
      index++;
    }
  }
  return result;
};
