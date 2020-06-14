var config = {
    wager: {
      value: 700, type: 'balance', label: 'wager'
    },
    payout: {
      value: 2, type: 'multiplier', label: 'payout' }
  };
  var game_history = [];
  var action = 1
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
  
  
  // Try to bet immediately when script starts
  //makeBet();
  
  engine.on('GAME_STARTING', onGameStarted);
  engine.on('GAME_ENDED', onGameEnded);
  
  

  function onGameStarted() {
    if (action == "0"){
      config.wager.value = 700
      makeBet();
      //console.log('action 1');
    } else if (action == 0) {
      config.wager.value = 700
      makeBet();
      console.log('actions 2');
    } else if (action == '2') {
      config.wager.value = 1400
      makeBet();
    } else if (action == 2) {
      config.wager.value = 1400
      makeBet();
    } else if (action == '3'){
      config.wager.value = 2100
      makeBet();
    } else if (action == 3) {
      config.wager.value = 2100
      makeBet();
    } else {
      config.wager.value = 700
      log("no buy");
    }
  };
  
  function onGameEnded() {
    var lastGame = engine.history.first();
    // If we wagered, it means we played
    if (game_history.length == 1001) {
      game_history.shift()
      game_history.push(lastGame.bust);
      

    } else {
      game_history.push(lastGame.bust);

    }
    if (game_history.length > 1000){
      var actions = postData('https://localhost:5000/predict', { gamearray: game_history })
      .then(data => {
        console.log(data);
        action = data.action // JSON data parsed by `response.json()` call

      });
      
    };
    
    log(game_history)
    if (!lastGame.wager) {
      return;
    }
    
  
    if (lastGame.cashedAt) {
      var profit = Math.round((config.wager.value * config.payout.value - config.wager.value) / 100)
      log('we won', profit, 'bits');
    } else {
      log('we lost', Math.round(config.wager.value / 100), 'bits');
    }
  }
  
  function makeBet() {
    engine.bet(config.wager.value, config.payout.value);
    log('betting', Math.round(config.wager.value / 100), 'on', config.payout.value, 'x');
  }

  //sujy8fo2r9