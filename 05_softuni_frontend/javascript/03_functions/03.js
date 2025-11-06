function printCharsInRange(char1, char2) {
  function getRange(start, end) {
    const result = [];
    const min = Math.min(start, end);
    const max = Math.max(start, end);

    for (let i = min + 1; i < max; i++) {
      result.push(String.fromCharCode(i));
    }

    return result.join(" ");
  }

  console.log(getRange(char1.charCodeAt(0), char2.charCodeAt(0)));
}
