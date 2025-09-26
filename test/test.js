const app = require("express")();
const supertest = require("supertest");
const request = supertest(app);

app.get("/", function (req, res) {
  res.status(200).send("practise with kubernetes"); // [cite: 50]
}); // [cite: 48, 49]

describe("GET /", function () { // [cite: 51, 52]
  it("should return 200 OK", function (done) { // [cite: 53, 54]
    request
      .get("/") // [cite: 56]
      .expect(200) // [cite: 57]
      .end(function (err, res) { // [cite: 58, 59]
        if (err) return done(err); // [cite: 60]
        done(); // [cite: 61]
      });
  });
});