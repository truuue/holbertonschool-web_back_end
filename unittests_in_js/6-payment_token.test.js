const getPaymentTokenFromAPI = require("./6-payment_token.js");

describe("getPaymentTokenFromAPI", () => {
  // Test case using done callback
  test("returns a successful response from the API when success is true", (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      try {
        expect(response).toEqual({ data: "Successful response from the API" });
        done();
        // it is crucial to call done to signal async test completion
      } catch (error) {
        done(error);
      }
    });
  });

  // Additional test to show how to handle when success is false
  test("does nothing when success is false", () => {
    expect(getPaymentTokenFromAPI(false)).toBeUndefined();
  });
});
