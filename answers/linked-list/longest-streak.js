const longestStreak = (head) => {
  if (!head) return 0;
  let value = head.val;
  let longest = 0;
  let count = 0;
  let current = head;
  while(current) {
    console.log(current.val, 'this is the current')
    if (current.val === value) {
      count++;
      console.log(count, 'count has increased')
      if (count > longest) {
        longest = count;
      }
    } else {
      value = current.val;
      count = 1;
      console.log('count has reset')
    }
    current = current.next;
  }
  return longest;
};
