function pascalCaseSplitter(str) {
  const words = str.match(/[A-Z][a-z]*/g);
  console.log(words.join(", "));
}

console.log(pascalCaseSplitter("SplitMeIfYouCanHaHaYouCantOrYouCan"));
