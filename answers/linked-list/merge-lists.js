const mergeLists = (head1, head2) => {
  let h1 = head1
  let h2 = head2
  let start; //to get access to head

  if (h1.val < h2.val) {
      start = h1;
      h1 = head1.next;
  } else {
      start = h2;
      h2 = head2.next;
  }

  let current = start;
  while (h1 !== null && h2 !== null) { //while there are nodes
      console.log(current.val, 'current value')
      if (h1.val < h2.val) {
          current.next = h1;
          h1 = h1.next;
      } else {
          current.next = h2;
          h2 = h2.next;
      }
      current = current.next;
  }
  if (!h1) {//sets the next node to the one that is not null;
      current.next = h2;
  } else {
      current.next = h1;
  }
  return start;
};
