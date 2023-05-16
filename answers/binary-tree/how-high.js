const howHigh = root => {
  if (!root) return -1;
  let left = howHigh(root?.left) || 0
  let right = howHigh(root?.right) || 0

  return 1 + Math.max(left, right);

}
