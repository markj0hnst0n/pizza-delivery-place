let timer2 = "2:01";
let interval = setInterval(function() {


  let timer = timer2.split(':');
  //by parsing integer, I avoid all extra string processing
  let minutes = parseInt(timer[0], 10);
  let seconds = parseInt(timer[1], 10);
  --seconds;
  minutes = (seconds < 0) ? --minutes : minutes;
  seconds = (seconds < 0) ? 59 : seconds;
  seconds = (seconds < 10) ? '0' + seconds : seconds;
  //minutes = (minutes < 10) ?  minutes : minutes;
  $('#countdown').html(minutes + ':' + seconds);
  if (minutes < 0) clearInterval(interval);
  //check if both minutes and seconds are 0
  if ((seconds <= 0) && (minutes <= 0))
    clearInterval(interval);
  timer2 = minutes + ':' + seconds;
  if (timer2 == '0:00') location.reload();
}, 1000);