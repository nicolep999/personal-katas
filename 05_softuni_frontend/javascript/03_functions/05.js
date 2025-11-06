function palindromeIntegers(arr) {
  arr.forEach((num) => {
    const reversed = Number(num.toString().split("").reverse().join(""));
    console.log(num === reversed);
  });
}
