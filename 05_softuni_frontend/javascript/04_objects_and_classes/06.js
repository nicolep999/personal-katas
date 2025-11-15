function wordTracker(arr) {
  let words = arr[0].split(" ");
  let wordsObj = {};
  for (let word of words) {
    wordsObj[word] = 0;
  }

  for (let i = 1; i < arr.length; i++) {
    let currentWord = arr[i];
    if (wordsObj.hasOwnProperty(currentWord)) {
      wordsObj[currentWord]++;
    }
  }

  let sortedWords = Object.entries(wordsObj).sort((a, b) => b[1] - a[1]);
  for (let [word, count] of sortedWords) {
    console.log(`${word} - ${count}`);
  }
}
