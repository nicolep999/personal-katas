function passwordValidator(password) {
  const isLengthValid = () => password.length >= 6 && password.length <= 10;
  const isOnlyLettersAndDigits = () => /^[A-Za-z0-9]+$/.test(password);
  const hasAtLeastTwoDigits = () => (password.match(/\d/g) || []).length >= 2;

  let isValid = true;

  if (!isLengthValid()) {
    console.log("Password must be between 6 and 10 characters");
    isValid = false;
  }

  if (!isOnlyLettersAndDigits()) {
    console.log("Password must consist only of letters and digits");
    isValid = false;
  }

  if (!hasAtLeastTwoDigits()) {
    console.log("Password must have at least 2 digits");
    isValid = false;
  }

  if (isValid) {
    console.log("Password is valid");
  }
}

// const passwordValidator = (password) => {
//   const rules = [
//     {
//       check: (p) => p.length >= 6 && p.length <= 10,
//       message: "Password must be between 6 and 10 characters",
//     },
//     {
//       check: (p) => /^[A-Za-z0-9]+$/.test(p),
//       message: "Password must consist only of letters and digits",
//     },
//     {
//       check: (p) => (p.match(/\d/g) || []).length >= 2,
//       message: "Password must have at least 2 digits",
//     },
//   ];

//   const failed = rules.filter((rule) => !rule.check(password));

//   if (failed.length === 0) {
//     console.log("Password is valid");
//   } else {
//     failed.forEach((rule) => console.log(rule.message));
//   }
// };
