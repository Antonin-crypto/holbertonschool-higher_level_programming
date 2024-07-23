/* document.addEventListener('DOMContentLoaded', (event) => { ... });
: Ce code s'assure que le script s'exécute seulement après que le document HTML est complètement chargé
et analysé, garantissant que l'élément header est disponible pour être sélectionné et modifié.*/
document.addEventListener('DOMContentLoaded', (event) => {
  // document.querySelector('header') : Cette méthode sélectionne le premier élément header trouvé dans le document HTML.
  const headerElement = document.querySelector('header');
  // headerElement.style.color = '#FF0000' : Cette ligne modifie la couleur du texte de l'élément header
  headerElement.style.color = '#FF0000';
});
