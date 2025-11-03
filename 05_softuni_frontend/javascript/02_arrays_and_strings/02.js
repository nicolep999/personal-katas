function everyNth(arr, step) {
  return arr.filter(function (_, i) {
    return i % step === 0;
  });
}
