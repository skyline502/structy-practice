const subsets = (elements) => {
  if (!elements.length) return [[]];

  const el = elements[0];
  const rest = elements.slice(1);
  const subsetsWithoutEl = subsets(rest);
  const subsetsWithEl = subsetsWithoutEl.map((sub) => [el, ...sub]);
  return [...subsetsWithoutEl, ...subsetsWithEl];
};
