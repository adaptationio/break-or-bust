async function makeBet() {
    let url = 'http://0.0.0.0:5000/predict';
    let response = await fetch(url);

    let commits = await response.json(); // read response body and parse as JSON

    console.log('post response',commits.prediction);
  }

const data = { username: 'example' };

fetch('https://localhost:5000/predict', {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});


// Example POST method implementation:
async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

postData('https://localhost:5000/predict', { gamearray: 42 })
  .then(data => {
    console.log(data); // JSON data parsed by `response.json()` call
  });

var myArray = [1, 2, 3];
var myJson = JSON.stringify(myArray); // "[1,2,3]"
....
xhr.send({
    data:{
        param: myJson
    }
});