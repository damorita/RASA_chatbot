var express = require("express");
var app = express();

// set directory for css files
app.use(express.static("public"));

// default set all files to render as ejs
app.set("view engine", "ejs");

// Home Page
app.get("/", function(req, res){
    res.render("home");
    // res.send("hi");
});


// Go to chat page
app.get("/AVA", function(req, res){
    res.render("ava");
});

// listen to port
app.listen(port=3000, function(){
    console.log('welcome to my app');
});



