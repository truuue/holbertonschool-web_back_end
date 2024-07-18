const request = require("request");
const url = "http://127.0.0.1:7865";

describe("Index page", () => {
  it("Good Status", (done) => {
    request(url, (err, res, body) => {
      assert.equal(res.statusCode, 200);
      done();
    });
  });

  it("Correct output", (done) => {
    request(url, (err, res, body) => {
      assert.equal(body, "Welcome to the payment system");
      done();
    });
  });

  it("No error response", (done) => {
    request(url, (err, res, body) => {
      assert.equal(err, null);
      done();
    });
  });
});
