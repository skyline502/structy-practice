const allTreePaths = (root) => {
  if (!root) return []; //if root is null;
  if (!root.left && !root.right) return [[root.val]];
  let paths = [];
  let leftPath = allTreePaths(root.left);
  for (let path of leftPath) {
    paths.push([root.val, ...path]);
  }
  let rightPath = allTreePaths(root.right);
  for (let path of rightPath) {
    paths.push([root.val, ...path]);
  }
  return paths;
};
