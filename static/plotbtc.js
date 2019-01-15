//
// Calculator
//
function plotbtc() {
    
    // Operator Selector
    place_sel = document.getElementById("place");
    var idx = place_sel.selectedIndex;
    var place = place_sel.options[idx].value;
    
    place2_sel = document.getElementById("place2");
    var idx2 = place2_sel.selectedIndex;
    var place2 = place2_sel.options[idx2].value;    
    
    place3_sel = document.getElementById("place3");
    var idx3 = place3_sel.selectedIndex;
    var place3 = place3_sel.options[idx3].value;

// Buid query parameter
    var param = {};
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    param["place"] = document.getElementById("place").value;
    param["place2"] = document.getElementById("place2").value;
    param["place3"] = document.getElementById("place3").value;
    param["aval"] = document.getElementById("aval").value;
    var query = jQuery.param(param);

// Query with a new parameter 
    $.get("/plot/btc" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};











//
// Register Event handler
//
document.getElementById("plot").addEventListener("click", function(){
    plotbtc() ;
}, false);

document.getElementById("start").addEventListener("chage", function(){
    plotbtc();
}, false);

document.getElementById("start").addEventListener("keyup", function(){
    plotbtc();
}, false);

document.getElementById("end").addEventListener("change", function(){
    plotbtc();
}, false);

document.getElementById("end").addEventListener("keyup", function(){
    plotbtc();
}, false);

document.getElementById("place").addEventListener("change", function(){
    plotbtc();
}, false);
document.getElementById("place2").addEventListener("change", function(){
    plotbtc();
}, false);
document.getElementById("place3").addEventListener("change", function(){
    plotbtc();
}, false);

document.getElementById("aval").addEventListener("change", function(){
    plotbtc();
}, false);
document.getElementById("aval").addEventListener("keyup", function(){
    plotbtc();
}, false);
//



plotbtc();
