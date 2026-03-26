document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
    const helloDiv = document.getElementById('hello');
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching translation:', error);
      });
  });