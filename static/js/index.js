var tabButtons = document.querySelectorAll('.box-top .tab button')
var tabPanels = document.querySelectorAll('.box-top .tabpanel')

function showPanel(panelIndex,colorcode){
    tabButtons.forEach(function(node){
        node.style.backgroundColor = "";
        node.style.color = ""
    });
    tabButtons[panelIndex].style.backgroundColor = colorcode
    tabButtons[panelIndex].style.color = "white"
    tabPanels.forEach(function(node){
        node.style.display ="none";
    })
    tabPanels[panelIndex].style.display = "flex"
}

<<<<<<< HEAD
showPanel(0,"#0A92DE")


=======
showPanel(0,"#0A92DE")
>>>>>>> 72b363b521e4db65a4b34b9a6ca8cf4ac85ffce0
