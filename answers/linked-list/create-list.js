const createLinkedList = arr => {
  if (!arr.length) {
    return null;
  }

  let prev = new Node(arr[0]);
  let head = prev;
  for (let i = 1; i < arr.length; i++) {
    let node = new Node(arr[i]);
    prev.next = node;
    prev = node;
  }
  return head;
}
