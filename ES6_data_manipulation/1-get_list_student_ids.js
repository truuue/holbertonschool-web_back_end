export default function getListStudentIds(arrayOfObjects) {
  let arrayOfIds = [];
  if (arrayOfObjects instanceof Array) {
    arrayOfIds = arrayOfObjects.map((object) => object.id);
  }
  return arrayOfIds;
}
