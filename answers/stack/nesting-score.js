const nestingScore = (str) => {
    //[] = 1 pt
    //[[]] = 2 * [[val]] //here val is 1, so 2 * 1 = 2
    //[[][]] = 2 * [[val][val]], here we have 2 val's so 2 * 2 = 4
    //use stack?
    let stack = [0];
    for (let char of str) {
        if (char === '[') {
            stack.push(0);
        } else {
          const popped = stack.pop();
          if (popped === 0) {
            stack[stack.length - 1] += 1;
          } else {
            stack[stack.length - 1] += 2 * popped;
          }
        }
    }
    return stack[stack.length - 1];
}
