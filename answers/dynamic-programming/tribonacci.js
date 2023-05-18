const tribonacci = (n, seq = {}) => {
  if (n === 0 || n === 1) return 0;
  if (n === 2) return 1;
  if (seq[n]) return seq[n];
  seq[n] = tribonacci(n - 1, seq) + tribonacci(n - 2, seq) + tribonacci(n - 3, seq);
  return seq[n];
};
