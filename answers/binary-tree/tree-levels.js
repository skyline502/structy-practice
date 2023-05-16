const treeLevels = (root) => {
  if (!root) return [];
  let levels = [];
  let stack = [{node: root, level: 0}];

  while (stack.length) {
      let current = stack.pop();
      if (!levels[current.level]) {
          levels.push([current.node.val]);
      } else {
          console.log(current.level, 'current level')
          console.log(levels, 'current levels')
          levels[current.level].push(current.node.val);
      }
      if (current.node.right) {
          stack.push({node: current.node.right, level: current.level + 1});
      }
      if (current.node.left) {
          stack.push({node: current.node.left, level: current.level + 1});
      }
  }

  return levels;
};
