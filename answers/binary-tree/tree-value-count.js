const treeValueCount = (root, target) => {
  if (!root) return 0;
  let count = 0;
  let stack = [root];
  while (stack.length) {
    let current = stack.pop();
    if (current.right) {
      stack.push(current.right);
    }
    if (current.left) {
      stack.push(current.left);
    }
    if (current.val === target) {
      count++;
    }
  }
  return count;
};

module.exports = {
  treeValueCount,
};
