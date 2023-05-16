const bottomRightValue = (root) => {
  let queue = [root];
  while (queue.length) {
    let current = queue.shift();
    if (!current.left && !current.right && !queue.length) {
      return current.val;
    }
    if (current.left) {
      queue.push(current.left);
    }
    if (current.right) {
      queue.push(current.right);
    }
  }
}
