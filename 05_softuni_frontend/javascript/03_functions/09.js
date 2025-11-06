function loadingBar(num) {
  let arr = new Array(10).fill(".");
  arr = arr.fill("%", 0, num / 10);

  if (num == 100) {
    console.log(`${num}% Complete!\n[${arr.join("")}]`);
  } else {
    console.log(`${num}% [${arr.join("")}]\nStill loading...`);
  }
}
