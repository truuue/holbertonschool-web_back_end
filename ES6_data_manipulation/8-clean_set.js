export default function cleanSet(set, startString) {
  let myString = '';
  if (startString === '' || typeof startString !== 'string') {
    return myString;
  }

  for (const value of set.values()) {
    if (value && value.startsWith(startString)) {
      myString += `${value.slice(startString.length)}-`;
    }
  }
  if (myString.endsWith('-')) {
    myString = myString.slice(0, -1);
  }
  return myString;
}
