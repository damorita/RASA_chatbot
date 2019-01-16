var express = require("express");
var app = express();

// set directory for css files
app.use(express.static("public"));

// default set all files to render as ejs
app.set("view engine", "ejs");



// Home Page
app.get("/", function(req, res){
    res.render("home");
});


// Go to chat page
app.get("/ava", function(req, res){
    res.render("ava");
});

// Go to Products page
app.get("/products", function(req, res){
    res.render("products");
});

// Go to teams page
app.get("/teams", function(req, res){
    res.render("teams");
});

// listen to port
app.listen(port=3000, function(){
    console.log('welcome to my app');
});



