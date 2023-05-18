const substituteSynonyms = (sentence, synonyms) => {
  let words = sentence.split(' ');
  const results = getWords(words, synonyms);
  return results.map(result => result.join(' '));
};

const getWords = (words, synonyms) => {
  if (!words.length) return [[]];

  const first = words[0];
  const rest = words.slice(1);

  if (first in synonyms) {
    let result = [];
    let remaining = getWords(rest, synonyms);

    for (let synonym of synonyms[first]) {
      result.push(...remaining.map(array => [synonym, ...array]));
    }

    return result;
  } else {
    let remaining = getWords(rest, synonyms);

    return remaining.map(array => [first, ...array]);
  }
}
