document.addEventListener('DOMContentLoaded', function() {
  // Select the translate button and add an event listener for the click event
  const btnTranslate = document.getElementById('btn_translate');
  btnTranslate.addEventListener('click', function() {
      // Get the selected language code from the combo box
      const languageCode = document.getElementById('language_code').value;
      // Construct the URL with the selected language code
      const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

      // Fetch the greeting in the selected language
      fetch(url)
          .then(response => response.json())  // Parse the JSON from the response
          .then(data => {
              // Select the HTML element with id 'hello'
              const helloDiv = document.getElementById('hello');
              // Set the text content of the element to the fetched 'hello' translation
              helloDiv.textContent = data.hello;
          })
          .catch(error => {
              console.error('Error fetching the greeting:', error);
          });
  });
});
