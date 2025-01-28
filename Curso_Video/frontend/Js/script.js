const exemploDiv = document.getElementById("exemplo");


// GET 
async function abu() {
    try {
        const response = await fetch('http://127.0.0.1:8000/course'); 
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        return data; 

    } catch (error) {
        console.error("Erro na requisição:", error);
        return `Erro ao obter dados ${error}`; 
    }
}

abu().then( retorno => {
    exemploDiv.innerHTML = JSON.stringify(retorno, null, 2);
});

// Post (estudem, tbm nao sei)
