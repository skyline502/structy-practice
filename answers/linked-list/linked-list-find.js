const linkedListFind = (head, target) => {
  if (head === null) return false;

  while(head) {
    if (head.val === target) {
      return true;
    } else {
      head = head.next;
    }
  }
  return false;
}
