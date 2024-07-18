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
      describe("GET /cart/:id", () => {
        it("Responds with 200 and payment methods for cart 8", (done) => {
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

        it("Responds with 200 and payment methods for cart 111", (done) => {
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

        it("Responds with 404 for invalid cart ID", (done) => {
          const options = {
            url: "http://localhost:7865/cart/k47",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
          });
        });

        it("Responds with 404 for non-existent cart ID", (done) => {
          const options = {
            url: "http://localhost:7865/cart/s56z",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
          });
        });

        it("Responds with 404 for invalid cart ID format", (done) => {
          const options = {
            url: "http://localhost:7865/cart/96a",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
          });
        });

        it("Responds with 404 for missing cart ID", (done) => {
          const options = {
            url: "http://localhost:7865/cart/hello",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
          });
        });

        it("Responds with 404 for empty cart ID", (done) => {
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

      describe("GET /login", () => {
        it("Responds with 200", (done) => {
          const options = {
            url: "http://localhost:7865/login",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
          });
        });
      });

      describe("GET /available_payments", () => {
        it("Responds with 200", (done) => {
          const options = {
            url: "http://localhost:7865/available_payments",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
          });
        });
      });
    });
  });
});
