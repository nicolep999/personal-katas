function heroesInventory(input) {
  const heroes = [];

  for (const line of input) {
    const [name, level, itemsString] = line.split(" / ");
    const items = itemsString
      ? itemsString.split(", ").filter((item) => item)
      : [];
    const hero = {
      name: name,
      level: Number(level),
      items: items,
    };
    heroes.push(hero);
  }

  for (const hero of heroes.sort((a, b) => a.level - b.level)) {
    console.log(
      `Hero: ${hero.name}\nlevel => ${hero.level}\nitems => ${hero.items.join(
        ", "
      )}`
    );
  }
}
