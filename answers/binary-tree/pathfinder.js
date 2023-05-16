const pathFinder = (root, target) => {
  let result = pathFinderResult(root, target);
  if (result === null) {
    return null;
  } else {
    console.log(result, 'result')
    return result.reverse();
  }
}

const pathFinderResult = (root, target) => {
  if (!root) return null;
  if (root.val === target) return [root.val];
  let rootLeft = pathFinderResult(root.left, target);
  let rootRight = pathFinderResult(root.right, target);

  if (rootLeft) {
    rootLeft.push(root.val);
    return rootLeft;
  }
 if (rootRight) {
    rootRight.push(root.val);
    return rootRight;
  }
  return null;
};
