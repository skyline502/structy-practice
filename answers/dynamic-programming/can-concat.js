const canConcat = (str, arr, memo = {}) => {
    //use indexOf to see if word in str is inside array
    //keep slicing str and see if current str can be indexed inside array
    //edge case if !str.length return true
    if (str in memo) return memo[str];
    if (str.length === 0) return true;
    for (let word of arr) {
      if (str.startsWith(word)) {
        const rest = str.slice(word.length);
        if (canConcat(rest, arr, memo)) {
          memo[str] = true;
          return true;
        }
      }
    }
  memo[str] = false;
  return false;
}
