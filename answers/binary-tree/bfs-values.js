const breadthFirstValues = (root) => {
  if (!root) {
    return [];
  }
  let values = [];
  let queue = [root];
  while(queue.length) {
    let current = queue.shift();
    if (current.left) {
      queue.push(current.left);
    }
    if (current.right) {
      queue.push(current.right);
    }
    values.push(current.val);
  }
  return values;
};
