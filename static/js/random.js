function getRandomPokemon(url){
    id = Math.floor((Math.random() * 647) + 1);
    window.location.href = url + "pokemon?name=" + id;
}