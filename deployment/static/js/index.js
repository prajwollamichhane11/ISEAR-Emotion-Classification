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

showPanel(0,"#0A92DE")