const zipperLists = (head1, head2) => {
  let current = head1;
  let next = head2;

  //a > x > b > y > c > z > d > e > f
  while (current) { //z
    let currentNext = current.next; //null
    if (next) {
      current.next = next;//z
    } else {
      break;
    }
    current = next; //z
    next = currentNext;//d
  }
  return head1;
};
