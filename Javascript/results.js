// (function() {
//   // selectors
//   links = document.querySelectorAll('a');
//
//   // set up a request
//   let request = new XMLHttpRequest();
//
//   for (let i = 0; i < links.length; i++) {
//     links[i].addEventListener('click', function() {
//       let request = new XMLHttpRequest();
//       request.onreadystatechange = alertContents;
//
//
//
//       request.open('GET', links[i].getAttribute('href'));
//       request.send();
//     });
//   }
//
//   function alertContents() {
//     if (httpRequest.readyState === XMLHttpRequest.DONE) {
//       if (httpRequest.status === 200) {
//         alert(httpRequest.responseText);
//       }
//       else {
//         alert('There was a problem with the request.');
//       }
//     }
//   }
//
//   // function getBody(content) {
//   //   let x = content.indexOf("<body");
//   //   x = content.indexOf(">", x);
//   //   let y = content.lastIndexOf("</body>");
//   //   return content.slice(x + 1, y);
//   // }
//   //
//   // function getContent(content, target)
//   // {
//   //   target.innerHTML =  getBody(content);
//   // }
//   //
//   // document.getElementById("displayed").innerHTML = responseHTML.innerHTML;
//   //
//   //
//
//
//
//
//
//
// })


(function() {

  // find the desired selectors
  let btn = document.getElementById('request');
  let bio = document.getElementById('bio');

  // set up a request
  let request = new XMLHttpRequest();

  // keep track of the request
  request.onreadystatechange = function() {
    // check if the response data send back to us
    if(request.readyState === 4) {
      // add a border
      bio.style.border = '1px solid #e8e8e8';
      // uncomment the line below to see the request
       console.log(request);
      // check if the request is successful
      if(request.status === 200) {
        // update the HTML of the element
        bio.innerHTML = request.responseText;
      } else {
        // otherwise display an error message
        bio.innerHTML = 'An error occurred during your request: ' +  request.status + ' ' + request.statusText;
      }
    }
  }

  // specify the type of request
  request.open('Get', 'http://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/Bio.txt');

  // register an event
  btn.addEventListener('click', function() {
    // hide the button
    this.style.display = 'none';
    // send the request
    request.send();
  });

})();
