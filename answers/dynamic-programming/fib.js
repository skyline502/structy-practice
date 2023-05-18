const fib = (n, seq = {}) => {
    if (n === 0) return 0;
    if (n === 1 || n === 2) return 1;
    if (seq[n]) return seq[n];
    seq[n] = fib(n - 1, seq) + fib(n - 2, seq);
    return seq[n];
}
