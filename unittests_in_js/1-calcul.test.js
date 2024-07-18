const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
  it("should return 6 when type is SUM, a is 1.4 and b is 4.5", function () {
    assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
  });

  it("should return -4 when type is SUBTRACT, a is 1.4 and b is 4.5", function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
  });

  it("should return 0.2 when type is DIVIDE, a is 1.4 and b is 4.5", function () {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
  });

  it("should return 6 when type is DIVIDE, a is 1.4 and b is 0", function () {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
  });
});
