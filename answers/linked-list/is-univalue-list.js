const isUnivalueList = (head) => {
  let value = head.val;
  while(head) {
    if (head.val !== value) {
      return false;
    }
    head = head.next;
  }
  return true;
};
