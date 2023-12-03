function searchSneakers() {
    const searchInput = document.getElementById('searchInput').value;

    // Make an AJAX request to your back end with the search input
    fetch('http://localhost:5000/api/search', {  // Update with your backend URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ searchInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Update the sneakerList with the fetched data
        updateSneakerList(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

function updateSneakerList(sneakers) {
    const sneakerList = document.getElementById('sneakerList');

    // Clear previous content
    sneakerList.innerHTML = '';

    // Iterate through the sneaker data and create cards
    sneakers.forEach(sneaker => {
        const sneakerCard = document.createElement('div');
        sneakerCard.classList.add('sneaker-card');
        sneakerCard.innerHTML = `<h3>${sneaker.model_name}</h3><p>${sneaker.price}</p>`;
        sneakerList.appendChild(sneakerCard);
    });
}
