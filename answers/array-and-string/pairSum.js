const pairSum = (numbers, targetSum) => {
  let seen = {};

  for (let i = 0; i < numbers.length; i++) {
    let num = numbers[i];
    let complement = targetSum - num;
    if (complement in seen) {
      return [i, seen[complement]];
    }
    seen[num] = i;
  }
  return seen;
}
