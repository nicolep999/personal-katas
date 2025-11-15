function storeProvision(currentStock, orderedStock) {
  const store = {};

  for (let i = 0; i < currentStock.length; i += 2) {
    const product = currentStock[i];
    const quantity = Number(currentStock[i + 1]);
    store[product] = quantity;
  }

  for (let i = 0; i < orderedStock.length; i += 2) {
    const product = orderedStock[i];
    const quantity = Number(orderedStock[i + 1]);

    if (store.hasOwnProperty(product)) {
      store[product] += quantity;
    } else {
      store[product] = quantity;
    }
  }

  for (const [product, quantity] of Object.entries(store)) {
    console.log(`${product} -> ${quantity}`);
  }
}
