// var restart = document.querySelector('#button1');
// var squares = document.querySelectorAll("td");
// function clearBoard()
// {
//     for(var i=0;i<squares.length;i++)
//     {
//         squares[i].textContent='';
//         console.log(squares[i].textContent);
//     }
// }

// if(restart)
// {
//     firtd=document.getElementById('ftd');
//     restart.addEventListener('click',firtd.textContent=' ');
//     restart.addEventListener('click',clearBoard);
// }
// Restart Game Button
var restart = document.querySelector('#button1');

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = ' ';
  }

}
restart.addEventListener('click',clearBoard);