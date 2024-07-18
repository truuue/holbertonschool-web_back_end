const express = require("express");
const app = express();
const port = 7865;

app.get("/", (req, res) => {
  res.end("Welcome to the payment system");
});

app.get("/cart/:id([0-9]+)", (req, res) => {
  res.end(`Payment methods for cart ${req.params.id}`);
});

app.listen(port, () => {
  console.log("API available on localhost port 7865");
});

app.get("/available_payments", (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

app.get("/login", (req, res) => {
  const userName = req.body.userName;
  res.send(`Welcome ${userName}`);
});
