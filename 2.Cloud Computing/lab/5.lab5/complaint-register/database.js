const mysql = require('mysql')
var options = {
    host     : 'localhost',
    user     : 'root',
    password : 'raj123SHANPK45',
    database : 'complaints',
    multipleStatements : true
  };

  var connection = mysql.createConnection(options)

  connection.connect((err) => {
      if(err){
          console.log(err);
          console.log('connection failed');
          return;
      }
      console.log('connected as id ' + connection.threadId);
  })

  module.exports = {connection,options}