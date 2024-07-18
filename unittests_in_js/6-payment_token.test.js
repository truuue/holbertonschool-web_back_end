const getPaymentTokenFromAPI = require("./6-payment_token.js");

describe("getPaymentTokenFromAPI", () => {
  test("returns a successful response from the API when success is true", (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      try {
        expect(response).toEqual({ data: "Successful response from the API" });
        done();
      } catch (error) {
        done(error);
      }
    });
  });

  test("does nothing when success is false", () => {
    expect(getPaymentTokenFromAPI(false)).toBeUndefined();
  });
});
