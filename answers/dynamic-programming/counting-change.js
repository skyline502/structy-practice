const countingChange = (amount, coins, i = 0, counts = {}) => {
  const key = amount + ',' + i;
  if (key in counts) return counts[key];

  if (amount === 0) return 1;
  if (i === coins.length) return 0;

  const coin = coins[i];
  let count = 0;


  for (let qty = 0; (qty * coin) <= amount; qty++) {
    const remainder = amount - (coin * qty);
    count += countingChange(remainder, coins, i + 1, counts);
  }
    counts[key] = count;
    return count;
};
