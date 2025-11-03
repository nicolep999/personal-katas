function modernTimes(str) {
  const regexp = /#([A-Za-z]+)/g;
  const matches = [...str.matchAll(regexp)];
  return matches.map((match) => match[1]).join("\n");
}
