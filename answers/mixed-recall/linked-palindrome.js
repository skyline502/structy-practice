const linkedPalindrome = (head) => {
  let list = [];

  let current = head;

  while(current) {
    list.push(current.val);
    current = current.next;
  }
  console.log(list.join(','))
  console.log(list.reverse())
  return list.join(',') === list.reverse().join(',');

}
