const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const path = require("path");
const { connection, options } = require("./database");

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  // database fetching
  // complaint form
  connection.query(
    `Select * from complainttable`,
    function (error, rows, fields) {
      if (!error) {
        res.render("home", { complaints: rows });
      }
    }
  );
  // const complaints = []
});

app.post("/register", (req, res) => {
  console.log("complaint register");
  const { complaint, name } = req.body;
  console.log(req.body);
  connection.query(
    `INSERT INTO complainttable(Complaint,Name) values('${complaint}','${name}')`,
    function (error, rows, fields) {
      if (!error) {
        res.redirect("/");
        return;
      }
    }
  );
});

app.listen(3000, (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log("server connected");
  }
});