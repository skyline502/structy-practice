const linkedListValues = (head) => {
  let values = [];

  while(head) {
    values.push(head.val);
    head = head.next;
  }

  return values;
};
