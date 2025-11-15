function employeesList(arr) {
  const employees = {};

  for (const name of arr) {
    employees[name] = name.length;
  }

  for (const [employeeName, personalNum] of Object.entries(employees)) {
    console.log(`Name: ${employeeName} -- Personal Number: ${personalNum}`);
  }
}
