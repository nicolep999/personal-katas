function factorialDivision(num1, num2) {
  const factorial = (n) => (n <= 1 ? 1 : n * factorial(n - 1));

  const result = factorial(num1) / factorial(num2);
  console.log(result.toFixed(2));
}
