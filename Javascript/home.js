howButton = document.querySelector('.how-to');
closeButton = document.querySelector('.close');
overlay = document.querySelector('.overlay');
image = document.querySelector('img');
content = document.querySelector('.content');
loginButton = document.querySelector('.button');

//
howButton.addEventListener('click', function() {
  overlay.style.height = '100%';
  image.classList.add('fadeInDown');
  content.style.marginTop = '-50px';
  loginButton.style.opacity = 0;
});

howButton.addEventListener('click', function() {
  overlay.style.height = '100%';
  image.classList.add('fadeInDown');
  content.style.marginTop = '-50px';
});


//
// closeButton.addEventListener('click', function() {
//   overlay.style.height = '0';
//   content.style.marginTop = '100px';
// });

overlay.addEventListener('click', function() {
  overlay.style.height = '0';
  content.style.marginTop = '100px';
  loginButton.style.opacity = 1.0;
});
