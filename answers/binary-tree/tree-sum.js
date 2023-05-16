const treeSum = (root) => {
  let sum = 0;
  if (!root) {
    return sum;
  }
  let stack = [root];

  while (stack.length) {
    let current = stack.pop();
    if (current.right) {
      stack.push(current.right);
    }
    if (current.left) {
      stack.push(current.left);
    }
    sum += current.val;
  }
  return sum;
};
