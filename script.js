
//send message to Background

chrome.runtime.sendMessage({name:"message"}, (response) => {
// Wait for response

console.log(response); 



});
