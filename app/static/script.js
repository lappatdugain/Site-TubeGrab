
// Sélectionner l'élément avec la classe "menu-hamburger".
const menuHamburger = document.querySelector(".menu-hamburger");
// Sélectionner l'élément avec la classe "nav-liens".
const navLiens = document.querySelector(".nav-liens");
// Ajouter un écouteur d'événements "click" à l'icône de menu hamburger.
menuHamburger.addEventListener('click', () => {
  // Au clic sur l'icône, ajouter ou supprimer la classe "mobile-menu" à l'élément avec la classe "nav-liens".
  // Cela permettra d'afficher ou de masquer le menu de navigation sur les appareils mobiles.
  navLiens.classList.toggle('mobile-menu');
});


document.addEventListener("DOMContentLoaded", function () {
    // Fonction pour changer la visibilité des formulaires en fonction du choix dans la liste déroulante
    function basculerVisibiliteFormulaire() {
        var choix = document.getElementById("choice_langue").value;
        var elementsEnglish = document.getElementsByClassName("english");
        var elementsFrench = document.getElementsByClassName("french");

        if (choix === "english") {
            // Traiter chaque élément individuellement ou choisir l'élément que vous souhaitez manipuler
            for (var i = 0; i < elementsEnglish.length; i++) {
                elementsEnglish[i].style.display = "block";
            }
            for (var i = 0; i < elementsFrench.length; i++) {
                elementsFrench[i].style.display = "none";
            }
        } else if (choix === "french") {
            // Traiter chaque élément individuellement ou choisir l'élément que vous souhaitez manipuler
            for (var i = 0; i < elementsEnglish.length; i++) {
                elementsEnglish[i].style.display = "none";
            }
            for (var i = 0; i < elementsFrench.length; i++) {
                elementsFrench[i].style.display = "block";
            }
        }
    }

    // Ajouter un écouteur d'événements sur la liste déroulante pour déclencher la fonction lorsqu'elle change
    document.getElementById("choice_langue").addEventListener("change", basculerVisibiliteFormulaire);

    // Appeler la fonction pour définir l'état initial
    basculerVisibiliteFormulaire();
});

document.getElementById('choice_mp3_mp4').addEventListener('change', function (e) {
    const urlInput = document.getElementById('url');
    urlInput.value = '';
    

    var elementsAlert = document.getElementsByClassName("alert-warning");
    for (var i = 0; i < elementsAlert.length; i++) {
        elementsAlert[i].style.display = "none";
    }
    
});


$(function () {
    // Get stored value or default to empty string
    var storedValue = localStorage.getItem('choice_mp3_mp4') || '';

    // Set stored value when page loads
    $('#choice_mp3_mp4').val(storedValue);

    // Store current value and reload page on change
    $('#choice_mp3_mp4').on('change', function () {
        var currValue = $(this).val();
        localStorage.setItem('choice_mp3_mp4', currValue);
        location.reload();
    });
});


