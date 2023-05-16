const leafList = (root) => {
  if (!root) return [];
  let leaves = [];
  let stack = [root];
  while (stack.length) {
      let current = stack.pop();
      if (!current.right && !current.left) {
          leaves.push(current.val);
      }
      if (current.right) {
          stack.push(current.right);
      }
      if (current.left) {
          stack.push(current.left);
      }
  }
  return leaves;
};
