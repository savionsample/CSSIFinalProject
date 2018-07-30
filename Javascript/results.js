var url = 'https://newsapi.org/v2/everything?sources=abc-news&q=climate-change&apiKey=756c841b3e2b4ce8bc345fd9da7a1caf'


var req = new Request(url);

fetch(req)
    .then(function(response) {
        console.log(response.json());
    })
