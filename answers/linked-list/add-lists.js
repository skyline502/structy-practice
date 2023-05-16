const addLists = (h1, h2) => {
  let h1values = [];
  let h2values = [];

  while (h1) {
    h1values.push(h1.val).toString();
    h1 = h1.next;
  }
  while(h2) {
    h2values.push(h2.val).toString();
    h2 = h2.next;
  }

  let sum = Number(h1values.reverse().join(''))+Number(h2values.reverse().join(''));
  sum = sum.toString().split('').reverse();
  // console.log(sum)

  let head = new Node(sum[0]);
  let current = head;

  for (let i = 1; i < sum.length; i++) {
    let node = new Node(sum[i]);
    current.next = node;
    current = current.next;
  }


  return head;
}
