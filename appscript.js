let token = "5405683249:AAHDOy3NcvFh6xKbwT7nBJ8M9h_XTiVdXKA";

function getMe() {
  let response = UrlFetchApp.fetch("https://api.telegram.org/bot" + token + "/getMe"); 
  console.log(response.getContentText());
}

function setWebhook() {
let webAppUrl = "https://script.google.com/macros/s/AKfycbzR2FUf7-eVUhRIr7rn1_QLehxZW6dh6lP8BZaly6fnaH_iQTKNWPZ-53VhGO_MECd3/exec";

let response = UrlFetchApp.fetch("https://api.telegram.org/bot" + token + "/setWebhook?url=" + webAppUrl); 
console.log(response.getContentText());
}

function doPost(e) {
  SpreadsheetApp.getActive().getActiveSheet().getRange(1,1).setValue(JSON.stringify(e,null,5));
  console.log(e);
  let contents = JSON.parse(e.postData.contents);
  let content = JSON.parse(e.postData.contents);
  SpreadsheetApp.getActive().getActiveSheet().getRange(1,1).setValue(JSON.stringify(contents,null,5));
  // SpreadsheetApp.getActive().getActiveSheet().getRange(1, 1).setValue(JSON.stringify(contents , null, 5));
}







// function myFunction() {
  
// }

// var token = "5405683249:AAHDOy3NcvFh6xKbwT7nBJ8M9h_XTiVdXKA"; 
// var telegramUrl = "https://api.telegram.org/bot" + token;
// var webAppUrl = "https://docs.google.com/spreadsheets/d/13UiNsVlVuDR8RMBLBeTzlvOGx83LG7cs78dPdv2OndQ/edit?usp=sharing";

// function setWebhook() {
// var url = telegramUrl + "/setWebhook?url=" + webAppUrl;
// var response = UrlFetchApp.fetch(url);
// }

// function sendMessage(chat_id, text) {
// var url = telegramUrl + "/sendMessage?chat_id=" + chat_id + "&text="+ text;
// var response = UrlFetchApp.fetch(url);
// Logger.log(response.getContentText()); 
// }

// function doPost(e) {
// var contents = JSON.parse(e.postData.contents);
// var chat_id = contents.message.from.id; 
// var text = "Beep boop bop, message received.";
 
// sendMessage(chat_id,text)

