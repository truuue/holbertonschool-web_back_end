const express = require("express");
const app = express();
const port = 7865;

app.use(express.json());

app.get("/", (req, res) => {
  res.end("Welcome to the payment system");
});

app.get("/cart/:id([0-9]+)", (req, res) => {
  res.end(`Payment methods for cart ${req.params.id}`);
});

app.get("/available_payments", (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

app.post("/login", (req, res) => {
  const userName = req.body.userName;
  if (!userName) {
    res.status(400).end("Bad Request");
    return;
  }
  res.end(`Welcome ${userName}`);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
