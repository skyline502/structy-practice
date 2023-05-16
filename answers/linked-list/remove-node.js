const removeNode = (head, targetVal) => {
  if (head.val === targetVal) {
    return head.next;
  }
  let current = head;
  while (current) {
    if (current.next.val === targetVal) {
      let next = current.next;
      current.next = next.next;
      return head;
    }
    current = current.next;
  }
};
