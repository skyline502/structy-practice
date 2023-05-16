const getNodeValue = (head, index) => {
  if (head === null) return null;
  if (index === 0) return head.val;
  console.log(head.next)
  return getNodeValue(head.next, index - 1)
}
