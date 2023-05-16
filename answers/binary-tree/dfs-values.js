const depthFirstValues = (root) => {
  let values = [];
  let stack = [root];
  if (!root) {
    return values;
  }
  while (stack.length) {
      let current = stack.pop();
      if(current.right) {
          stack.push(current.right)
      }
      if(current.left) {
          stack.push(current.left);
      }
      values.push(current.val)
  }
  return values;
};
