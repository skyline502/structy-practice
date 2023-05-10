/*

parenthetical possibilities
Write a function, parentheticalPossibilities, that takes in a string as an argument. The function should return an array containing all of the strings that could be generated by expanding all parentheses of the string into its possibilities.

For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.

test_00:
parentheticalPossibilities('x(mn)yz'); // ->
// [ 'xmyz', 'xnyz' ]
test_01:
parentheticalPossibilities("(qr)ab(stu)c"); // ->
// [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]
test_02:
parentheticalPossibilities("taco"); // ->
// ['taco']
test_03:
parentheticalPossibilities(""); // ->
// ['']
test_04:
parentheticalPossibilities("(etc)(blvd)(cat)"); // ->
// [
//  'ebc', 'eba', 'ebt', 'elc', 'ela',
//  'elt', 'evc', 'eva', 'evt', 'edc',
//  'eda', 'edt', 'tbc', 'tba', 'tbt',
//  'tlc', 'tla', 'tlt', 'tvc', 'tva',
//  'tvt', 'tdc', 'tda', 'tdt', 'cbc',
//  'cba', 'cbt', 'clc', 'cla', 'clt',
//  'cvc', 'cva', 'cvt', 'cdc', 'cda',
//  'cdt'
// ]
const parentheticalPossibilities = (s) => {
  if (!s.length) return [''];

  const allPossiblities = [];

  const { choices, remainder } = getChoices(s);
  for (let choice of choices) {
    const remainderPossibilities = parentheticalPossibilities(remainder);
    for (let substring of remainderPossibilities) {
      allPossiblities.push(choice + substring);
    }
  }

  return allPossiblities;
};

const getChoices = (s) => {
  if (s[0] === '(') {
    const end = s.indexOf(')');
    const choices = s.slice(1, end);
    const remainder = s.slice(end + 1);
    return {
      choices,
      remainder
    }
  } else {
    return {
      choices: s[0],
      remainder: s.slice(1)
    };
  }
}

*/
