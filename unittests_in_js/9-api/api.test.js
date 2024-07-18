const request = require("request");
const { expect } = require("chai");

describe("Integration Testing", () => {
  describe("GET /", () => {
    it("Code: 200 | Body: Welcome to the payment system", (done) => {
      const options = {
        url: "http://localhost:7865",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal("Welcome to the payment system");
        done();
      });
    });
  });

  describe("GET /cart/12", () => {
    it("Responds with 200 and id 12 in msg", (done) => {
      const options = {
        url: "http://localhost:7865/cart/12",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal("Payment methods for cart 12");
        done();
      });
    });
  });

  describe("GET /cart/8", () => {
    it("Responds with 200 and id 1 in msg", (done) => {
      const options = {
        url: "http://localhost:7865/cart/8",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal("Payment methods for cart 8");
        done();
      });
    });
  });

  describe("GET /cart/111", () => {
    it("Responds with 200 and id 12 in msg", (done) => {
      const options = {
        url: "http://localhost:7865/cart/111",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal("Payment methods for cart 111");
        done();
      });
    });
  });

  describe("GET /cart/k47", () => {
    it("Responds with 404", (done) => {
      const options = {
        url: "http://localhost:7865/cart/k47",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe("GET /cart/s56z", () => {
    it("Responds with 404", (done) => {
      const options = {
        url: "http://localhost:7865/cart/s56z",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe("GET /cart/96a", () => {
    it("Responds with 404", (done) => {
      const options = {
        url: "http://localhost:7865/cart/96a",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe("GET /cart/hello", () => {
    it("Responds with 404", (done) => {
      const options = {
        url: "http://localhost:7865/cart/hello",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe("GET /cart/", () => {
    it("Responds with 404", (done) => {
      const options = {
        url: "http://localhost:7865/cart/",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
