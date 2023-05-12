/*

exical order
Write a function, lexicalOrder, that takes in 2 words and an alphabet string as an argument. The function should return true if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return false.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

test_00:
const alphabet = "abcdefghijklmnopqrstuvwxyz";
lexicalOrder("apple", "dock", alphabet); // -> true
test_01:
const alphabet = "abcdefghijklmnopqrstuvwxyz";
lexicalOrder("apple", "ample", alphabet); // -> false
test_02:
const alphabet = "abcdefghijklmnopqrstuvwxyz";
lexicalOrder("app", "application", alphabet); // -> true
test_03:
const alphabet = "abcdefghijklmnopqrstuvwxyz";
lexicalOrder("backs", "backdoor", alphabet); // -> false
test_04:
const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
lexicalOrder("zoo", "dinner", alphabet); // -> true
test_05:
const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
lexicalOrder("leaper", "leap", alphabet); // -> false
test_06:
const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
lexicalOrder("backs", "backdoor", alphabet); // -> true
test_07:
const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
lexicalOrder("semper", "semper", alphabet); // -> true

*/
