const intersection = (a, b) => {
  let result = [];
  let nums = new Set(a);
  for (let i = 0; i < b.length; i++) {
    let num = b[i];
    if (nums.has(num)) {
      result.push(num);
    }
  }
  return result;
};
