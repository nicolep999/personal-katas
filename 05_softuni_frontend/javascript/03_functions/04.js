function OddAndEvenSum(num) {
  let arr = Array.from(String(num), Number);

  odd_sum = arr.filter((el) => el % 2 != 0).reduce((a, b) => a + b, 0);
  even_sum = arr.filter((el) => el % 2 == 0).reduce((a, b) => a + b, 0);
  console.log(`Odd sum = ${odd_sum}, Even sum = ${even_sum}`);
}
