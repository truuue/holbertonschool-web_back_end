export default function updateUniqueItems(groceries) {
    const newGroceries = new Map();
    groceries.forEach((value, key) => {
        if (value === 1) {
        newGroceries.set(key, value);
        }
    });
    return newGroceries;
}
