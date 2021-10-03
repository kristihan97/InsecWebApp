var navElements = ["hjem", "om oss", "meny", "kultur", "kontakt"];
var navAdd = ["./index.html", "./omOss.html", "./meny.html", "./kultur.html", "./kontaktOss.html"];

const createNavBar = () =>{
    const container = document.getElementById("nav-container");
    const navRight = document.createElement("div");
    navRight.className = "menu-list-right";
    const navLeft = document.createElement("div");
    navLeft.className = "name";
    const logo = document.createElement("a");
    logo.textContent = "soil";
    logo.href = "./index.html";
    logo.setAttribute("target", "_self");
    navLeft.appendChild(logo);  
    const elListe = document.createElement("ul");

    for (var i = 0; i < navElements.length; i++) {
        var element = navElements[i];
        var adresse = navAdd[i];
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.textContent = element;
        a.href = adresse;
        a.setAttribute("target", "_self")
        li.appendChild(a);
        elListe.appendChild(li);
    };

    navRight.appendChild(elListe);
    container.appendChild(navLeft);
    container.appendChild(navRight);

}

createNavBar();

window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
  
    // 20 is an arbitrary number here, just to make you think if you need the prevScrollpos variable:
    if (currentScrollPos > 20) {
      // I am using 'display' instead of 'top':
      document.getElementById("nav-scroll").style.display = "none";
    } else {
      document.getElementById("nav-scroll").style.display = "initial";
    }
  }

  let current_url = document.location;
  document.querySelectorAll(".menu-list-right a").forEach(function(e){
     if(e.href == current_url){
        e.classList += " current";
     }
  });