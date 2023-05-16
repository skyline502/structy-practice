const treeMinValue = (root) => {
  let min = root.val;
  let stack = [root];
  while (stack.length) {
    let current = stack.pop();
    if (current.right) {
      stack.push(current.right);
    }
    if (current.left) {
      stack.push(current.left);
    }
    if (current.val < min) {
      min = current.val;
    }
  }
  return min;
};
