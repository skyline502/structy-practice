const insertNode = (head, value, index) => {
  let i = 0;
  let newNode = new Node(value);
  let current = head;
  let prev = null;
  if (index === 0) {
    newNode.next = head;
    return newNode;
  }
  while (i <= index) {
    if (i === index) {
      if (!current) {
          prev.next = newNode;
          return head;
      }
      let next = current.next;
      prev.next = newNode;
      newNode.next = current;
      return head;
    }
    prev = current;
    current = current.next;
    i++;
  }
};
