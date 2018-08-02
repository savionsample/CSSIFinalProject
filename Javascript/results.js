
let button = document.querySelector(".need");
console.log(button);

let url = "http://google.com" //this will have to connect to the news api instead of a hard link
  button.addEventListener('click', e => {
       window.fetch('/results?q=' + encodeURIComponent(url)).then(
         response => response.text()).then(text => {
           console.log(text);
         });
  });

// I think there might have to be a urlfetch.fetch instead of a window.fetch component.
// instead of reponse.text maybe it should actually be reponse.json()).then(json => need.innerText = json.need;)
//or within the fetch portion is where you add the api key from mercury?
