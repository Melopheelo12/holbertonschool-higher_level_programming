// Select the element that will be clicked
const redHeaderTrigger = document.querySelector('#red_header');

// Select the header element that will receive the new class
const headerElement = document.querySelector('header');

// Add an event listener for the 'click' event
redHeaderTrigger.addEventListener('click', () => {
  headerElement.classList.add('red');
});