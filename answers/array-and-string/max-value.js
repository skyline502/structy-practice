const maxValue = (nums) => {
  let max = -Infinity;

  for (let val of nums) {
    if (val > max) {
      max = val;
    }
  }

  return max;
};
