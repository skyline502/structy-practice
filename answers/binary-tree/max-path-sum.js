const maxPathSum = (root) => {
  if (!root) return -Infinity;
  if (!root.left && !root.right) return root.val;
  let maxChildSum = Math.max(maxPathSum(root.left), maxPathSum(root.right));
  return root.val + maxChildSum;
};
