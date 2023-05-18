const pairedParentheses = (s) => {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        console.log(count, 'count')
        if (count < 0) return false;
        if (char === '(') {
            count++;
        } else if (char === ')') {
            count--;
        }
    }
    return count === 0;
}
