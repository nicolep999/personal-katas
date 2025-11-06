function sum(first, second, third) {
  function subtract(result, third) {
    return result - third;
  }

  const result = first + second;
  return subtract(result, third);
}
