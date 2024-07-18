// Create test case

const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", () => {
  it("should return 4 when inputs are 1 and 3", function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it("should return 5 when inputs are 1 and 3.7", function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it("should return 5 when inputs are 1.2 and 3.7", function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it("should return 6 when inputs are 1.5 and 3.7", function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it("should return 0 when inputs are -0.4 and 0.4", function () {
    assert.strictEqual(calculateNumber(-0.4, 0.4), 0);
  });

  it("should return -1 when inputs are -0.6 and -0.4", function () {
    assert.strictEqual(calculateNumber(-0.6, -0.4), -1);
  });

  it("should return -2 when inputs are -1.4 and -0.6", function () {
    assert.strictEqual(calculateNumber(-1.4, -0.6), -2);
  });

  it("should return -2 when inputs are -1.5 and -1.4", function () {
    assert.strictEqual(calculateNumber(-1.5, -1.4), -2);
  });

  it("should return 1 when inputs are -1.5 and 2.4", function () {
    assert.strictEqual(calculateNumber(-1.5, 2.4), 1);
  });
});
