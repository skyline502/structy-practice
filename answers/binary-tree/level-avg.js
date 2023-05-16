const levelAverages = (root) => {
  if (!root) return [];
    let levels = {};
    let stack = [{node: root, level: 0}];
    while(stack.length) {
        let current = stack.pop();
        if (!levels[current.level]) {
            levels[current.level] = [current.node.val];
        } else {
            levels[current.level].push(current.node.val);
        }
        if (current.node.right) {
            stack.push({node: current.node.right, level: current.level + 1});
        }
        if (current.node.left) {
            stack.push({node: current.node.left, level: current.level + 1});
        }
    }
    let avg = [];
    for (val in levels) {
        let sum = levels[val].reduce((a,b) => a + b, 0);
        avg[val] = sum / levels[val].length;
    }
    return avg;
}
