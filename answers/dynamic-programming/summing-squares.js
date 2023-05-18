const summingSquares = (n, squares = {}) => {
  if (n in squares) return squares[n];
  if (n === 0) return 0;
  let minSquares = Infinity;

  for (let i = 1; i <= Math.sqrt(n); i++) {
    let square = i * i;
    let numSquares = 1 + summingSquares(n - square, squares);
    minSquares = Math.min(minSquares, numSquares);
  }
  squares[n] = minSquares;
  return squares[n];
};
