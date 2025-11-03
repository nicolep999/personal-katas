function revealWords(wordsStr, sentence) {
  let words = wordsStr.split(",").map((w) => w.trim());

  words.forEach((word) => {
    let regex = new RegExp(`\\*{${word.length}}`);
    sentence = sentence.replace(regex, word);
  });

  return sentence;
}
