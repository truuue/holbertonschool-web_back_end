const assert = require("assert");
const { add, subtract, multiply, divide } = require("./0-calcul");

describe("Calculator", () => {
  describe("add", () => {
    it("should return the sum of two numbers", () => {
      assert.strictEqual(add(2, 3), 5);
      assert.strictEqual(add(-1, 5), 4);
      assert.strictEqual(add(0, 0), 0);
    });
  });

  describe("subtract", () => {
    it("should return the difference between two numbers", () => {
      assert.strictEqual(subtract(5, 2), 3);
      assert.strictEqual(subtract(10, -5), 15);
      assert.strictEqual(subtract(0, 0), 0);
    });
  });

  describe("multiply", () => {
    it("should return the product of two numbers", () => {
      assert.strictEqual(multiply(2, 3), 6);
      assert.strictEqual(multiply(-2, 5), -10);
      assert.strictEqual(multiply(0, 10), 0);
    });
  });

  describe("divide", () => {
    it("should return the quotient of two numbers", () => {
      assert.strictEqual(divide(6, 2), 3);
      assert.strictEqual(divide(10, -5), -2);
      assert.strictEqual(divide(0, 10), 0);
    });

    it("should throw an error when dividing by zero", () => {
      assert.throws(() => divide(5, 0), Error, "Cannot divide by zero");
    });
  });
});
