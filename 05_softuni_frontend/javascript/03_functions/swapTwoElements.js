function completeArrSwap(arr) {
  for (let i = 0; i < arr.length / 2; i++) {
    swapTwoElements(arr, i, -i);
  }
  function swapTwoElements(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}
