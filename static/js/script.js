/*const postsContainer = document.getElementById('posts-container');
const loader = document.getElementById('loader');

let ready = false;
let currentPage = 1;

// Unsplash API for "women empowerment" photos
const query = 'women empowerment';
const apiKey = 'UdORU5qqxfVt46EqG06N7kehRES-PwuVSuLP57tON80'; 
// Replace with your valid API key
const apiUrl = `https://api.unsplash.com/search/photos?query=${encodeURIComponent(query)}&per_page=10&client_id=${apiKey}`;

// Fetch photos from Unsplash
async function fetchPhotos(page) {
    loader.classList.remove('hidden'); // Show loader
    try {
        const response = await fetch(${apiUrl}&page=${page});
        const data = await response.json();
        displayPhotos(data.results);
        loader.classList.add('hidden'); // Hide loader
        ready = true;
    } catch (error) {
        console.error('Error fetching photos:', error);
    }
}

// Render photos dynamically
function displayPhotos(photos) {
    photos.forEach((photo) => {
        const photoElement = document.createElement('div');
        photoElement.classList.add('post');
        photoElement.innerHTML = `
            <a href="${photo.links.html}" target="_blank">
                <img src="${photo.urls.regular}" alt="${photo.alt_description || 'Photo'}" title="${photo.alt_description || 'Photo'}">
            </a>
            <h3>${photo.alt_description || 'Untitled'}</h3>
        `;
        postsContainer.appendChild(photoElement);
    });
}

// Infinite scroll logic
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000 && ready) {
        ready = false;
        currentPage++;
        fetchPhotos(currentPage);
    }
});

// Initial load
fetchPhotos(currentPage);*/



const postsContainer = document.getElementById('posts-container');
const loader = document.getElementById('loader');

let ready = false;
let currentPage = 1;

// Unsplash API for "women empowerment" photos
const query = 'women empowerment';
const apiKey = 'UdORU5qqxfVt46EqG06N7kehRES-PwuVSuLP57tON80'; 
// Replace with your valid API key
const apiUrl = `https://api.unsplash.com/search/photos?query=${encodeURIComponent(query)}&per_page=10&client_id=${apiKey}`;

// Fetch photos from Unsplash
async function fetchPhotos(page) {
    loader.classList.remove('hidden'); // Show loader
    try {
        const response = await fetch(`${apiUrl}&page=${page}`);
        const data = await response.json();
        displayPhotos(data.results);
        loader.classList.add('hidden'); // Hide loader
        ready = true;
    } catch (error) {
        console.error('Error fetching photos:', error);
    }
}

// Render photos dynamically
function displayPhotos(photos) {
    photos.forEach((photo) => {
        const photoElement = document.createElement('div');
        photoElement.classList.add('post');
        photoElement.innerHTML = `
            <a href="${photo.links.html}" target="_blank">
                <img src="${photo.urls.regular}" alt="${photo.alt_description || 'Photo'}" title="${photo.alt_description || 'Photo'}">
            </a>
            <h3>${photo.alt_description || 'Untitled'}</h3>
        `;
        postsContainer.appendChild(photoElement);
    });
}

// Infinite scroll logic
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000 && ready) {
        ready = false;
        currentPage++;
        fetchPhotos(currentPage);
    }
});

// Initial load
fetchPhotos(currentPage);
