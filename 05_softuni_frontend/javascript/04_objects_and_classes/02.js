function townsInfo(arr) {
  for (const line of arr) {
    const [town, latitude, longitude] = line.split(" | ");
    const townObj = {
      town: town,
      latitude: Number(latitude).toFixed(2),
      longitude: Number(longitude).toFixed(2),
    };
    console.log(townObj);
  }
}
