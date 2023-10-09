export default function cleanSet(set, startString) {
  const newSet = new Set();
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      newSet.add(value.slice(startString.length));
    }
  });
  return newSet;
}
