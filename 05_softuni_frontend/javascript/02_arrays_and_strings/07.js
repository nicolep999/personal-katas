function stringSubstring(word, str) {
  const lowerWord = word.toLowerCase();
  const words = str.split(" ");
  for (const w of words) {
    if (w.toLowerCase() === lowerWord) {
      return lowerWord;
    }
  }
  return `${word} not found!`;
}
