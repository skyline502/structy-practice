const decompressBraces = (s) => {
    //find {}
    //then take the number before { as i, do loop and repeat what is between {}
    //set rest var to what is after }
    //do recursion on rest
    if (!s.includes('{')) return s;
    let result = '';
    let start;
    let end;
    let multiplier;
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (char === '{') {
            start = i + 1;
            multiplier = s[i - 1];
        }
        if (char === '}') {
            end = i;
            let string = s.slice(start, end);
            result += s.slice(0, start - 2) + string.repeat(multiplier);
            return result + decompressBraces(s.slice(end + 1));
        }
    }
}
