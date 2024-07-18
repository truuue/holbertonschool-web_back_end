const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./5-payment");

describe("sendPaymentRequestToApi", function () {
  let calculateNumberStub;
  let consoleLogSpy;

  beforeEach(function () {
    calculateNumberStub = sinon.stub(Utils, "calculateNumber");
    consoleLogSpy = sinon.spy(console, "log");
  });

  afterEach(function () {
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });

  it('logs "The total is: 120" when called with 100 and 20', function () {
    calculateNumberStub.withArgs("SUM", 100, 20).returns(120);
    sendPaymentRequestToApi(100, 20);

    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWith("The total is: 120")).to.be.true;
  });

  it('logs "The total is: 20" when called with 10 and 10', function () {
    calculateNumberStub.withArgs("SUM", 10, 10).returns(20);
    sendPaymentRequestToApi(10, 10);

    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWith("The total is: 20")).to.be.true;
  });
});
