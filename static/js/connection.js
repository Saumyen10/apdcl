var division = document.querySelector('#division');
var sdivision = document.querySelector('#sdivision');
var options2 = sdivision.querySelectorAll('option');

function giveSelection(selValue) {
  sdivision.innerHTML = '';
  for(var i = 0; i < options2.length; i++) {
    if(options2[i].dataset.option === selValue) {
      sdivision.appendChild(options2[i]);
    }
  }
}

giveSelection(division.value);