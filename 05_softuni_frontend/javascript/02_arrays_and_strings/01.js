function arrayRotation(arr, n) {
  n = n % arr.length;
  return arr.slice(n).concat(arr.slice(0, n)).join(" ");
}
