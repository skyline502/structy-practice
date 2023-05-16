const uncompress = (s) => {
  const nums = '0123456789'
  let result = '';
  let multiple = '';

  for (let char of s) {
    if (nums.includes(char)) {
      multiple += char;
    } else {
      result += char.repeat(multiple);
      multiple = '';
    }
  }

  return result;

};
