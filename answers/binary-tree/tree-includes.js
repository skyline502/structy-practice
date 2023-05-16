const treeIncludes = (root, target) => {
  if (!root) {
      return false;
  }
  let queue = [root];
  while (queue.length) {
      let current = queue.shift();
      if (current.val === target) {
          return true;
      }
      if (current.left) {
          queue.push(current.left);
      };
      if (current.right) {
          queue.push(current.right);
      }
  }
  return false;
};
