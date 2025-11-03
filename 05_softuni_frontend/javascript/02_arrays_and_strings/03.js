function listOfNames(arr) {
  arr.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: "base" }));
  arr.forEach((element, index) => {
    console.log(`${index + 1}.${element}`);
  });
}
