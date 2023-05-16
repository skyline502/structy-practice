const pairProduct = (numbers, targetProduct) => {
  let seen = {};
  for (let i = 0; i < numbers.length; i++) {
      let num = numbers[i];
      let complement = targetProduct / num;

      if (complement in seen) {
          return [i, seen[complement]]
      }

      seen[num] = i;
  }
};
