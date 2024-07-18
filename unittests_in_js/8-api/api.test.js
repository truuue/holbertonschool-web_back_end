const request = require("request");
const chai = require("chai");
const expect = chai.expect;

describe("Index page", () => {
  const url = "http://localhost:7865/";

  it("Correct status code?", (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("Correct result?", (done) => {
    request.get(url, (error, response, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
});
