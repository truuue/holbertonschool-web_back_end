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

  describe("GET /cart/:id", () => {
    it("Responds with 200 and correct message", (done) => {
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

    it("Responds with 404 for invalid id", (done) => {
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

  describe("GET /available_payments", () => {
    it("Responds with 200 and correct payment methods", (done) => {
      const options = {
        url: "http://localhost:7865/available_payments",
        method: "GET",
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        const expectedResponse = {
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        };
        expect(JSON.parse(body)).to.deep.equal(expectedResponse);
        done();
      });
    });
  });

  describe("POST /login", () => {
    it("Responds with 200 and correct welcome message", (done) => {
      const options = {
        url: "http://localhost:7865/login",
        method: "POST",
        json: {
          userName: "Betty",
        },
        headers: {
          "Content-Type": "application/json",
        },
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(response.body).to.equal("Welcome Betty");
        done();
      });
    });

    it("Responds with 400 for missing userName", (done) => {
      const options = {
        url: "http://localhost:7865/login",
        method: "POST",
        json: {},
        headers: {
          "Content-Type": "application/json",
        },
      };

      request(options, function (error, response, body) {
        expect(response.statusCode).to.equal(400);
        expect(body).to.equal("Bad Request");
        done();
      });
    });
  });
});
