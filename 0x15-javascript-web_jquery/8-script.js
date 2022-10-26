$.get('https://swapi-api.hbtn.io/api/films/?format=json', fuction (data) {
 $('UL#list_movies').append(...data.results.map(movie => '<li>${movie.title}</li>'));
});
