const minChange = (target, coins) => {
  let result = _minChange(target, coins);
  console.log(result)
  if (result === Infinity) {
    return -1;
  } else {
    return result;
  }
};

const _minChange = (target, coins, memo = {}) => {
  if (target === 0) return 0;
  if (target < 0) return Infinity;
  if (target in memo) return memo[target];
  let minCoins = Infinity;

  for (let coin of coins) {
    let numCoins = 1 + _minChange(target - coin, coins, memo);
    if (numCoins < minCoins) {
      minCoins = numCoins;
    }
  }
  memo[target] = minCoins;
  return minCoins;
}
