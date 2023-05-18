const permutations = (items) => {
  if (!items.length) return [[]];
  let first = items[0];
  let rest = permutations(items.slice(1));

  let permutation = []
  for (let item of rest) {
    for (let i = 0; i <= item.length; i++) {
      permutation.push([...item.slice(0, i), first, ...item.slice(i)])
    }
  }
  return permutation;
};
