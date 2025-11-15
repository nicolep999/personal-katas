function oddOccurrences(input) {
  if (Array.isArray(input)) {
    input = input[0];
  }

  let words = input.toLowerCase().split(" ");
  let countObj = {};

  for (let word of words) {
    countObj[word] = (countObj[word] || 0) + 1;
  }

  let result = [];
  for (let word of words) {
    if (countObj[word] % 2 !== 0 && !result.includes(word)) {
      result.push(word);
    }
  }

  console.log(result.join(" "));
}
oddOccurrences(`Java C# Php PHP Java PhP 3 C# 3 1 5 C#`);
